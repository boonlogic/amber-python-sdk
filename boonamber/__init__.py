import itertools
import json
import os
from collections.abc import Iterable
from numbers import Number, Integral
import requests


############################
# Boon Amber Python SDK v1 #
############################


class AmberUserError(Exception):
    """Raised to indicate an error in SDK usage"""

    def __init__(self, message):
        self.message = message


class AmberCloudError(Exception):
    """Raised upon any non-200 response from the Amber cloud"""

    def __init__(self, code, message):
        self.code = code
        self.mesage = message


class AmberClient():
    def __init__(self, license_id='default', license_file="~/.Amber.license"):
        """Main client which interfaces with the Amber cloud

        Args:
            license_id (str): license identifier label found within .Amber.license configuration file
            license_file (str): path to .Amber.license file
        
        Environment:
            AMBER_LICENSE_FILE: sets license_file path
            AMBER_LICENSE_ID: sets license_id
            AMBER_USERNAME: overrides the username as found in .Amber.license file
            AMBER_PASSWORD: overrides the password as found in .Amber.license file
            AMBER_SERVER: overrides the server as found in .Amber.license file
        """

        self.server = "https://amber-local.boonlogic.com/dev"
        self.token = None

        env_license_file = os.environ['AMBER_LICENSE_FILE']
        env_license_id = os.environ['AMBER_LICENSE_ID']
        env_username = os.environ['AMBER_USERNAME']
        env_password = os.environ['AMBER_PASSWORD']
        env_server = os.environ['AMBER_SERVER']

        # if username, password and server are all specified via environment, we're done here
        if all([env_username, env_password, env_server]):
            self.username = env_username
            self.password = env_password
            self.server = env_server
            return

        # otherwise, we acquire some or all of them from license file
        license_file = env_license_file if env_license_file else license_file
        license_id = env_license_id if env_license_id else license_id

        license_path = os.path.expanduser(license_file)
        if not os.path.exists(license_path):
            raise AmberUserError("license file {} does not exist".format(license_path))

        try:
            with open(license_path, 'r') as f:
                file_data = json.load(f)
        except json.JSONDecodeError as e:
            raise AmberUserError("JSON formatting error in license file: {}, line: {}, col: {}".format(e.msg, e.lineno, e.colno))

        try:
            license_data = file_data[license_id]
        except KeyError:
            raise AmberUserError("license_id '{}' not found in license file".format(license_id))

        # load the username, password and server, still giving precedence to environment
        try:
            self.username = env_username if env_username else license_data['username']
        except KeyError:
            raise AmberUserError("'username' is missing from the specified license in license file")

        try:
            self.password = env_password if env_password else license_data['password']
        except KeyError:
            raise AmberUserError("'password' is missing from the specified license in license file")

        try:
            self.server = env_server if env_server else license_data['server']
        except KeyError:
            raise AmberUserError("'server' is missing from the specified license in license file")

    def authenticate(self):
        """Authenticate client for the next hour using the credentials given at
        initialization. This acquires and stores an oauth2 token which remains
        valid for one hour and is used to authenticate all other API requests.

        Raises:
            AmberCloudError: if Amber cloud gives non-200 response
        """

        url = self.server + '/oauth2'
        headers = {
            'Content-Type': 'application/json'
        }
        body = {
            'username': self.username,
            'password': self.password
        }

        response = requests.request(method='POST', url=url, headers=headers, json=body)

        if response.status_code != 200:
            raise AmberCloudError(response.status_code, response.json()['message'])

        # invalid credentials are a 200 but token is an empty string
        if not response.json()['idToken']:
            raise AmberCloudError(401, "invalid credentials")

        self.token = response.json()['idToken']

    def _api_call(self, method, url, headers, body=None):
        """Make a REST call to the Amber server and handle the response"""

        response = requests.request(method=method, url=url, headers=headers, json=body)

        if response.status_code != 200:
            raise AmberCloudError(response.status_code, response.json())

        # todo: why are 404 errors returning 200 status codes with error
        # codes/message in body instead? this if block should not be needed
        if 'code' in response.json() and response.json()['code'] != 200:
            raise AmberCloudError(response.json()['code'], response.json()['message'])

        # lambda runtime errors return 200 with errorMessage in response body
        if 'errorMessage' in response.json():
            raise AmberCloudError(500, response.json()['errorMessage'])

        return response.json()

    def create_sensor(self, label=''):
        """Create a new sensor instance

        Args:
            label (str): label to assign to created sensor

        Returns:
            sensor_id (str): sensor-id of newly created sensor

        Raises:
            AmberUserError: if client is not authenticated
            AmberCloudError: if Amber cloud gives non-200 response
        """

        if self.token is None:
            raise AmberUserError("authentication required")

        url = self.server + '/sensor'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.token),
        }
        body = {
            'label': label
        }
        response = self._api_call('POST', url, headers, body=body)
        sensor_id = response['sensor-id']

        return sensor_id

    def delete_sensor(self, sensor_id):
        """Delete an amber sensor instance

        Args:
            sensor_id (str): sensor identifier

        Raises:
            AmberUserError: if client is not authenticated
            AmberCloudError: if Amber cloud gives non-200 response
        """

        if self.token is None:
            raise AmberUserError("authentication required")

        url = self.server + '/sensor'
        headers = {
            'Authorization': 'Bearer {}'.format(self.token),
            'sensor-id': sensor_id
        }
        response = self._api_call('DELETE', url, headers)

    def list_sensors(self):
        """List all sensor instances currently associated with Amber account

        Returns:
            sensors (dict): dict mapping sensor-ids to corresponding labels if
                successful, error string otherwise

        Raises:
            AmberUserError: if client is not authenticated
            AmberCloudError: if Amber cloud gives non-200 response
        """

        if self.token is None:
            raise AmberUserError("authentication required")

        url = self.server + '/sensors'
        headers = {
            'Authorization': 'Bearer {}'.format(self.token),
        }
        response = self._api_call('GET', url, headers)
        sensors = {s['sensor-id']: s['label'] for s in response}

        return sensors

    def configure_sensor(self, sensor_id, features=1, streaming_window_size=25,
                         samples_to_buffer=10000,
                         learning_rate_numerator=10,
                         learning_rate_denominator=10000,
                         learning_max_clusters=1000,
                         learning_max_samples=1000000):
        """Configure an amber sensor instance

        Args:
            sensor_id (str): sensor identifier
            features (int): number of features (dimensionality of each data sample)
            streaming_window_size (int): streaming window size (number of samples)
            samples_to_buffer (int): number of samples to load before autotuning
            learning_rate_numerator (int): sensor "graduates" (i.e. transitions from
                learning to monitoring mode) if fewer than learning_rate_numerator
                new clusters are opened in the last learning_rate_denominator samples
            learning_rate_denominator (int): see learning_rate_numerator
            learning_max_clusters: sensor graduates if this many clusters are created
            learning_max_samples: sensor graduates if this many samples are processed

        Returns:
            config (dict): newly applied configuration

        Raises:
            AmberUserError: if client is not authenticated or supplies invalid options
            AmberCloudError: if Amber cloud gives non-200 response
        """
        if self.token is None:
            raise AmberUserError("authentication required")

        if not features > 0 or not isinstance(features, Integral):
            raise AmberUserError("invalid 'feature_count': must be positive integer")

        if not streaming_window_size > 0 or not isinstance(streaming_window_size, Integral):
            raise AmberUserError("invalid 'streaming_window_size': must be positive integer")

        url = self.server + '/config'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.token),
            'sensor-id': sensor_id
        }
        body = {
            'features': features,
            'streamingWindowSize': streaming_window_size,
            'enableAutoTuning': True,
            'samplesToBuffer': samples_to_buffer,
            'learningGraduation': True,
            'learningRateNumerator': learning_rate_numerator,
            'learningRateDenominator': learning_rate_denominator,
            'learningMaxClusters': learning_max_clusters,
            'learningMaxSamples': learning_max_samples
        }
        config = self._api_call('POST', url, headers, body=body)

        return config

    def _isiterable(self, x):
        # consider strings non-iterable for shape validation purposes,
        # then they are printed out whole when caught as nonnumeric
        if isinstance(x, str):
            return False

        # collections.abc docs: "The only reliable way to determine
        # whether an object is iterable is to call iter(obj)."
        try:
            iter(x)
        except TypeError:
            return False

        return True

    def _validate_dims(self, data):
        """Validate that data is non-empty and one of the following:
           scalar value, list-like or list-of-lists-like where all
           sublists have equal length. Return 0, 1 or 2 as inferred
           number of array dimensions
        """

        # not-iterable data is a single scalar data point
        if not self._isiterable(data):
            return 0

        # iterable and unnested data is a 1-d array
        if not any(self._isiterable(d) for d in data):
            if len(list(data)) == 0:
                raise ValueError("empty")

            return 1

        # iterable and nested data is 2-d array
        if not all(self._isiterable(d) for d in data):
            raise ValueError("cannot mix nested scalars and iterables")

        sublengths = [len(list(d)) for d in data]
        if len(set(sublengths)) > 1:
            raise ValueError("nested sublists must have equal length")

        flattened_2d = list(itertools.chain.from_iterable(data))

        if any(isinstance(i, Iterable) for i in flattened_2d):
            raise ValueError("cannot be nested deeper than list-of-lists")

        if sublengths[0] == 0:
            raise ValueError("empty")

        return 2

    def _convert_to_csv(self, data):
        """Validate data and convert to a comma-separated plaintext string"""

        # Note: as in the Boon Nano SDK, there is no check that data dimensions
        # align with number of features and streaming window size.
        ndim = self._validate_dims(data)

        if ndim == 0:
            data_flat = [data]
        elif ndim == 1:
            data_flat = list(data)
        elif ndim == 2:
            data_flat = list(itertools.chain.from_iterable(data))

        for d in data_flat:
            if not isinstance(d, Number):
                raise ValueError("contained {} which is not numeric".format(d.__repr__()))

        return ','.join([str(float(d)) for d in data_flat])

    def stream_sensor(self, sensor_id, data):
        """Stream data to an amber sensor and return the inference result

        Args:
            sensor_id (str): sensor identifier
            data (array-like): data to be inferenced. Must be non-empty,
                entirely numeric and one of the following: scalar value,
                list-like or list-of-lists-like where all sublists have
                equal length.

        Returns:
            results (dict): resulting inferences. Contains:
                'state' (str): state of the sensor. "Starting" = gathering initial
                    sensor data, "Autotuning" = autotuning configuration in progress,
                    "Learning" = sensor is active and learning, "Monitoring" = sensor
                    is active but monitoring only (learning disabled)
                'SI' (list): smoothed anomaly index. The values in this list correspond
                    one-for-one with input samples and range between 0.0 and 1.0. Values
                    closer to 0 represent input patterns which are ordinary given the data
                    seen so far on this sensor. Values closer to 1 represent novel patterns
                    which are anomalous with respect to data seen before.

        Raises:
            AmberUserError: if client is not authenticated or supplies invalid data
            AmberCloudError: if Amber cloud gives non-200 response
        """

        if self.token is None:
            raise AmberUserError("authentication required")

        # Server expects data as a plaintext string of comma-separated values.
        try:
            data_csv = self._convert_to_csv(data)
        except ValueError as e:
            raise AmberUserError("invalid data: {}".format(e))

        url = self.server + '/stream'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.token),
            'sensor-id': sensor_id
        }
        body = {
            'data': data_csv
        }

        results = self._api_call('POST', url, headers, body=body)

        # normalize smooth index from the range [0, 1000] to [0.0, 1.0]
        results['SI'] = [r / 1000.0 for r in results['SI']]

        return results

    def get_sensor(self, sensor_id):
        """Get info about a sensor

        Args:
            sensor_id (str): sensor identifier

        Returns:
            sensor (dict): sensor info dict. Contains:
                'label': sensor label
                'sensor-id': sensor identifier
                'tenant-id': username of associated Amber account

        Raises:
            AmberUserError: if client is not authenticated
            AmberCloudError: if Amber cloud gives non-200 response
        """
        if self.token is None:
            raise AmberUserError("authentication required")

        url = self.server + '/sensor'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.token),
            'sensor-id': sensor_id
        }
        sensor = self._api_call('GET', url, headers)

        return sensor

    def get_config(self, sensor_id):
        """Get current sensor configuration

        Args:
            sensor_id (str): sensor identifier

        Returns:
            config (dict): current sensor configuration

        Raises:
            AmberUserError: if client is not authenticated
            AmberCloudError: if Amber cloud gives non-200 response
        """
        if self.token is None:
            raise AmberUserError("authentication required")

        url = self.server + '/config'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.token),
            'sensor-id': sensor_id
        }
        config = self._api_call('GET', url, headers)

        return config

    def get_status(self, sensor_id):
        """Get sensor status

        Args:
            sensor_id (str): sensor identifier

        Returns:
            status (dict): status dict if successful, error string otherwise:
                'pca' (list): list of length-3 vectors representing cluster centroids
                    with dimensionality reduced to 3 principal components
                'cluster-growth' (list): list of sample indexes at which new clusters were created
                'cluster-sizes' (list): list containing the number of samples in each cluster
                'anomaly-indexes' (list): list containing the anomaly index associated with each cluster
                'frequency-indexes' (list): list containing the frequency index associated with each cluster
                'distance-indexes' (list): list containing the distance index associated with each cluster
                'total-inferences' (int): total number of inferences performed so far
                'average-inference-time' (float): average inference time in microseconds
                'num-clusters' (int): number of clusters created so far

        Raises:
            AmberUserError: if client is not authenticated
            AmberCloudError: if Amber cloud gives non-200 response
        """
        if self.token is None:
            raise AmberUserError("authentication required")

        url = self.server + '/status'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.token),
            'sensor-id': sensor_id
        }
        status = self._api_call('GET', url, headers)

        return status
