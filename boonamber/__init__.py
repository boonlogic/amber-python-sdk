import itertools
from collections.abc import Iterable
from numbers import Number, Integral
import requests


############################
# Boon Amber Python SDK v1 #
############################


_AMBER_URL = "https://yr15pccsn4.execute-api.us-east-1.amazonaws.com/dev-python"
_amber_creds = {
    'api_key': None,
    'api_tenant': None,
    'is_set': False
}


class BoonException(Exception):
    def __init__(self, message):
        self.message = message


def _api_call(method, url, headers, body=None):
    """Make a REST call to the Amber server and handle the response"""

    try:
        response = requests.request(method=method, url=url, headers=headers, json=body)
    except Exception as e:
        return False, "request failed: {}".format(e)

    if response.status_code != 200:
        return False, '{}: {}'.format(response.status_code, response.json())

    # backend errors return 200 with errorMessage in response body
    if 'errorMessage' in response.json():
        return False, "server error: {}".format(response.json()['errorMessage'])

    return True, response.json()['body']


def set_credentials(api_key, api_tenant):
    """Set the API credentials to be used for Amber calls
    
    Args:
        api_key (str): API authentication key
        api_tenant (str): API tenant identifier
    """
    if not isinstance(api_key, str):
        raise BoonException("invalid credentials: 'api_key' must be a string")

    if not isinstance(api_tenant, str):
        raise BoonException("invalid credentials: 'api_tenant' must be a string")

    _amber_creds['api_key'] = api_key
    _amber_creds['api_tenant'] = api_tenant
    _amber_creds['is_set'] = True


def create_sensor(sensor_id):
    """Create a new sensor instance

    Args:
        sensor_id (str): sensor identifier

    Returns:
        success (bool): True if operation was successful
        response (str): amber server response
    """

    if not _amber_creds['is_set']:
        raise BoonException("credentials not set")

    url = _AMBER_URL + '/sensor'
    headers = {
        'x-token': _amber_creds['api_key'],
        'api-tenant': _amber_creds['api_tenant'],
        'sensor-id': sensor_id
    }
    return _api_call('POST', url, headers)


def delete_sensor(sensor_id):
    """Delete an amber sensor instance

    Args:
        sensor_id (str): sensor identifier

    Returns:
        success (bool): True if operation was successful
        response (str): amber server response
    """

    if not _amber_creds['is_set']:
        raise BoonException("credentials not set")

    url = _AMBER_URL + '/sensor'
    headers = {
        'x-token': _amber_creds['api_key'],
        'api-tenant': _amber_creds['api_tenant'],
        'sensor-id': sensor_id
    }
    return _api_call('DELETE', url, headers)


def list_sensors():
    """List all sensor instances associated with current API credentials

    Returns:
        success (bool): True if operation was successful
        response (list): list of sensor-ids if successful, error string otherwise
    """

    if not _amber_creds['is_set']:
        raise BoonException("credentials not set")

    url = _AMBER_URL + '/sensors'
    headers = {
        'x-token': _amber_creds['api_key'],
        'api-tenant': _amber_creds['api_tenant'],
    }
    return _api_call('GET', url, headers)


def configure_sensor(sensor_id, feature_count=1, streaming_window=25):
    """Configure an amber sensor instance

    Args:
        sensor_id (str): sensor identifier
        feature_count (int): number of features (dimensionality of each data sample)
        streaming_window (int): streaming window size (number of samples)

    Returns:
        success (bool): True if operation was successful
        response (dict): config dict if successful, error string otherwise
    """
    if not _amber_creds['is_set']:
        raise BoonException("credentials not set")

    if not feature_count > 0 or not isinstance(feature_count, Integral):
        raise BoonException("invalid 'feature_count': must be positive integer")

    if not streaming_window > 0 or not isinstance(feature_count, Integral):
        raise BoonException("invalid 'streaming_window': must be positive integer")

    url = _AMBER_URL + '/config'
    headers = {
        'x-token': _amber_creds['api_key'],
        'api-tenant': _amber_creds['api_tenant'],
        'sensor-id': sensor_id
    }
    body = {
        'accuracy': 0.99,
        'features': [
            {
                'minVal': 0,
                'maxVal': 1,
                'weight': 1
            } for f in range(feature_count)],
        'numericFormat': 'float32',
        'percentVariation': 0.05,
        'streamingWindowSize': streaming_window,
    }
    return _api_call('POST', url, headers, body=body)


def _isiterable(x):
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


def _validate_dims(data):
    """Validate that data is non-empty and one of the following:
       scalar value, list-like or list-of-lists-like where all
       sublists have equal length. Return 0, 1 or 2 as inferred
       number of array dimensions
    """

    # not-iterable data is a single scalar data point
    if not _isiterable(data):
        return 0

    # iterable and unnested data is a 1-d array
    if not any(_isiterable(d) for d in data):
        if len(list(data)) == 0:
            raise ValueError("empty")

        return 1

    # iterable and nested data is 2-d array
    if not all(_isiterable(d) for d in data):
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

def _convert_to_csv(data):
    """Validate data and convert to a comma-separated plaintext string"""

    # Note: as in the Boon Nano SDK, there is no check that data dimensions
    # align with feature_count and streaming_window.
    ndim = _validate_dims(data)

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


def stream_sensor(sensor_id, data):
    """Stream data to an amber sensor and return the inference result

    Args:
        sensor_id (str): sensor identifier
        data (array-like): data to be inferenced. Must be non-empty,
            entirely numeric and one of the following: scalar value,
            list-like or list-of-lists-like where all sublists have
            equal length.

    Returns:
        success (bool): True if operation was successful
        response (dict): results dict if successful, error string otherwise
    """

    if not _amber_creds['is_set']:
        raise BoonException("credentials not set")

    # Server expects data as a plaintext string of comma-separated values.
    try:
        data_csv = _convert_to_csv(data)
    except ValueError as e:
        raise BoonException("invalid data: {}".format(e))

    url = _AMBER_URL + '/stream'
    headers = {
        'x-token': _amber_creds['api_key'],
        'api-tenant': _amber_creds['api_tenant'],
        'sensor-id': sensor_id
    }
    body = {
        'data': data_csv
    }

    success, results = _api_call('POST', url, headers, body=body)
    if not success:
        return success, results

    # normalize from the range [0, 1000] to [0.0, 1.0]
    results = [r / 1000.0 for r in results['SI']]

    # if input data is scalar, results are scalar too
    if not _isiterable(data):
        return results[0]
    return results


def train_sensor(sensor_id, data):
    """Train an amber sensor on given data

    Args:        
        sensor_id (str): sensor identifier
        data (array-like): data to be inferenced. Must be non-empty,
            entirely numeric and one of the following: scalar value,
            list-like or list-of-lists-like where all sublists have
            equal length.
    
    Returns:
        succeess (bool): True if operation was successful
        response (str): amber server response
    """

    if not _amber_creds['is_set']:
        raise BoonException("credentials not set")

    # Server expects data as a plaintext string of comma-separated values.
    try:
        data_csv = _convert_to_csv(data)
    except ValueError as e:
        raise BoonException("invalid data: {}".format(e))

    url = _AMBER_URL + '/train'
    headers = {
        'x-token': _amber_creds['api_key'],
        'api-tenant': _amber_creds['api_tenant'],
        'sensor-id': sensor_id
    }
    body = {
        'data': data_csv
    }

    return _api_call('POST', url, headers, body=body)


def get_info(sensor_id):
    """Get usage info about a sensor

    Args:
        sensor_id (str): sensor identifier

    Returns:
        succeess (bool): True if operation was successful
        response (dict): config dict if successful, error string otherwise
    """
    if not _amber_creds['is_set']:
        raise BoonException("credentials not set")

    url = _AMBER_URL + '/sensor'
    headers = {
        'x-token': _amber_creds['api_key'],
        'api-tenant': _amber_creds['api_tenant'],
        'sensor-id': sensor_id
    }
    return _api_call('GET', url, headers)


def get_config(sensor_id):
    """Get current sensor configuration

    Args:
        sensor_id (str): sensor identifier

    Returns:
        succeess (bool): True if operation was successful
        response (dict): config dict if successul, error string otherwise
    """
    if not _amber_creds['is_set']:
        raise BoonException("credentials not set")

    url = _AMBER_URL + '/config'
    headers = {
        'x-token': _amber_creds['api_key'],
        'api-tenant': _amber_creds['api_tenant'],
        'sensor-id': sensor_id
    }
    return _api_call('GET', url, headers)


def get_status(sensor_id):
    """Get sensor status

    Args:
        sensor_id (str): sensor identifier

    Returns:
        succeess (bool): True if operation was successful
        response (dict): status dict if successful, error string otherwise
    """
    if not _amber_creds['is_set']:
        raise BoonException("credentials not set")

    url = _AMBER_URL + '/status'
    headers = {
        'x-token': _amber_creds['api_key'],
        'api-tenant': _amber_creds['api_tenant'],
        'sensor-id': sensor_id
    }
    return _api_call('GET', url, headers)
