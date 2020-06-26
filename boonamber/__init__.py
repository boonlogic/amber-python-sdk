import itertools
from collections.abc import Iterable
from numbers import Number, Integral
import requests


############################
# Boon Amber Python SDK v1 #
############################


class BoonException(Exception):
    def __init__(self, message):
        self.message = message


class AmberClient():
    def __init__(self):
        self.url = "https://amber-local.boonlogic.com/dev"
        self.token = None

    def authenticate(self, username, password):
        """Authenticate client for the next hour using Amber account
        credentials. This acquires and stores an oauth2 Bearer token which
        remains valid for one hour and is used to authenticate all other
        API requests.

        Args:
            username: Amber account name
            password: Amber account password

        Returns:
            success (bool): True if operation was successful
            response (None): None if successful, error string otherwise
        """

        url = self.url + '/oauth2'
        headers = {
            'Content-Type': 'application/json'
        }
        body = {
            'username': username,
            'password': password
        }

        response = requests.request(method='POST', url=url, headers=headers, json=body)

        if response.status_code != 200:
            return False, '{}: {}'.format(response.status_code, response.json()['message'])

        # invalid credentials are a 200 but token is an empty string
        if not response.json()['id-token']:
            return False, "401: invalid credentials"

        self.token = response.json()['id-token']
        return True, None

    def _api_call(self, method, url, headers, body=None):
        """Make a REST call to the Amber server and handle the response"""

        response = requests.request(method=method, url=url, headers=headers, json=body)

        if response.status_code != 200:
            return False, '{}: {}'.format(response.status_code, response.json())

        # todo: why are 404 errors returning 200 status codes with error
        # codes/message in body instead? this if block should not be needed
        if 'code' in response.json() and response.json()['code'] != 200:
            return False, '{}: {}'.format(response.json()['code'], response.json()['message'])

        # lambda runtime errors return 200 with errorMessage in response body
        if 'errorMessage' in response.json():
            return False, "500: {}".format(response.json()['errorMessage'])

        return True, response.json()

    def create_sensor(self, label=''):
        """Create a new sensor instance

        Args:
            label (str): label to assign to created sensor

        Returns:
            success (bool): True if operation was successful
            response (str): sensor-id if successful, error string otherwise
        """

        if self.token is None:
            raise BoonException("authentication required")

        url = self.url + '/sensor'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.token),
        }
        body = {
            'label': label
        }
        success, response = self._api_call('POST', url, headers, body=body)

        if not success:
            return False, response

        return True, response['sensor-id']

    def delete_sensor(self, sensor_id):
        """Delete an amber sensor instance

        Args:
            sensor_id (str): sensor identifier

        Returns:
            success (bool): True if operation was successful
            response (str): amber server response
        """

        if self.token is None:
            raise BoonException("authentication required")

        url = self.url + '/sensor'
        headers = {
            'Authorization': 'Bearer {}'.format(self.token),
            'sensor-id': sensor_id
        }
        success, response = self._api_call('DELETE', url, headers)

        if not success:
            return False, response

        return True, response['message']

    def list_sensors(self):
        """List all sensor instances associated with current API credentials

        Returns:
            success (bool): True if operation was successful
            response (dict): dict mapping sensor-ids to corresponding labels if
                successful, error string otherwise
        """

        if self.token is None:
            raise BoonException("authentication required")

        url = self.url + '/sensors'
        headers = {
            'Authorization': 'Bearer {}'.format(self.token),
        }
        success, response = self._api_call('GET', url, headers)

        if not success:
            return False, response

        response = {s['sensor-id']: s['label'] for s in response}
        return True, response

    def configure_sensor(self, sensor_id, features=1, streaming_window_size=25,
                         samples_to_buffer=10000,
                         learning_graduation=True,
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
            learning_graduation (bool): whether to "graduate", i.e. transition
                from learning to monitoring mode
            learning_rate_numerator (int): sensor graduates if fewer than
                learning_rate_numerator new clusters are opened in the last 
                learning_rate_denominator samples
            learning_rate_denominator (int): see larning_rate_numerator
            learning_max_clusters: sensor graduates if this many clusters are created
            learning_max_samples: sensor graduates if this many samples are processed

        Returns:
            success (bool): True if operation was successful
            response (dict): config dict if successful, error string otherwise
        """
        if self.token is None:
            raise BoonException("authentication required")

        if not features > 0 or not isinstance(features, Integral):
            raise BoonException("invalid 'feature_count': must be positive integer")

        if not streaming_window_size > 0 or not isinstance(streaming_window_size, Integral):
            raise BoonException("invalid 'streaming_window_size': must be positive integer")

        url = self.url + '/config'
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
            'learningGraduation': learning_graduation,
            'learningRateNumerator': learning_rate_numerator,
            'learningRateDenominator': learning_rate_denominator,
            'learningMaxClusters': learning_max_clusters,
            'learningMaxSamples': learning_max_samples
        }
        return self._api_call('POST', url, headers, body=body)

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
            success (bool): True if operation was successful
            response (dict): results dict if successful, error string otherwise:
                'state' (str): state of the sensor. "Starting" = gathering initial
                    sensor data, "Autotuning" = autotuning configuration in progress,
                    "Learning" = sensor is active and learning, "Monitoring" = sensor
                    is active but monitoring only (learning disabled)
                'SI' (list): smoothed anomaly index. The values in this list correspond
                    one-for-one with input samples and range between 0.0 and 1.0. Values
                    closer to 0 represent input patterns which are ordinary given the data
                    seen so far on this sensor. Values closer to 1 represent novel patterns
                    which are anomalous with respect to data seen before.
        """

        if self.token is None:
            raise BoonException("authentication required")

        # Server expects data as a plaintext string of comma-separated values.
        try:
            data_csv = self._convert_to_csv(data)
        except ValueError as e:
            raise BoonException("invalid data: {}".format(e))

        url = self.url + '/stream'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.token),
            'sensor-id': sensor_id
        }
        body = {
            'data': data_csv
        }

        success, response = self._api_call('POST', url, headers, body=body)
        if not success:
            return False, response

        # normalize smooth index from the range [0, 1000] to [0.0, 1.0]
        response['SI'] = [r / 1000.0 for r in response['SI']]
        return success, response

    def get_sensor(self, sensor_id):
        """Get info about a sensor

        Args:
            sensor_id (str): sensor identifier

        Returns:
            succeess (bool): True if operation was successful
            response (dict): sensor info dict if successful, error string otherwise
        """
        if self.token is None:
            raise BoonException("authentication required")

        url = self.url + '/sensor'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.token),
            'sensor-id': sensor_id
        }
        return self._api_call('GET', url, headers)

    def get_config(self, sensor_id):
        """Get current sensor configuration

        Args:
            sensor_id (str): sensor identifier

        Returns:
            succeess (bool): True if operation was successful
            response (dict): config dict if successul, error string otherwise
        """
        if self.token is None:
            raise BoonException("authentication required")

        url = self.url + '/config'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.token),
            'sensor-id': sensor_id
        }
        return self._api_call('GET', url, headers)

    def get_status(self, sensor_id):
        """Get sensor status

        Args:
            sensor_id (str): sensor identifier

        Returns:
            succeess (bool): True if operation was successful
            response (dict): status dict if successful, error string otherwise:
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

        """
        if self.token is None:
            raise BoonException("authentication required")

        url = self.url + '/status'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.token),
            'sensor-id': sensor_id
        }
        return self._api_call('GET', url, headers)
