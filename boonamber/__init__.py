import itertools
from collections.abc import Iterable
from numbers import Number
import requests


###########################
# BoonAmber Python API v1 #
###########################


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
    _amber_creds['api_key'] = api_key
    _amber_creds['api_tenant'] = api_tenant
    _amber_creds['is_set'] = True


def create_sensor(sensor_id):
    """Creates new sensor instance

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
    """Deletes an amber sensor instance

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
    """Lists all sensor instances associated with current API credentials

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


def configure_sensor(sensor_id, feature_count, streaming_window):
    """Configures an amber sensor instance

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


def _flatten_data(data):
    """Turn array-like data into a flat list"""

    # if data isn't iterable, treat as a single scalar data point
    if not isinstance(data, Iterable):
        return [data]

    # data is a nested list, flatten using itertools
    if any(isinstance(d, Iterable) for d in data):
        if not all(isinstance(d, Iterable) for d in data):
            raise BoonError("bad data: cannot mix nested scalars and iterables")

        return list(itertools.chain.from_iterable(data))

    return list(data)


def _validate_numeric(data):
    """Validate that data (iterable) contains only numerics"""

    for d in data:
        if not isinstance(d, Number):
            raise BoonError("bad data: contained {} which is not numeric".format(d.__repr__()))

    return data


def stream_sensor(sensor_id, data):
    """Streams data to an amber sensor and returns the inference result

    Args:
        sensor_id (str): sensor identifier
        data (array-like): data to be inferenced. Must be array-like in
            that it is a numeric scalar, list-like, or list-of-lists-like
            which has no side effects if iterated.

    Returns:
        success (bool): True if operation was successful
        response (dict): results dict if successful, error string otherwise
    """

    if not _amber_creds['is_set']:
        raise BoonException("credentials not set")

    # server expects data flattened as a string of comma-separated values
    # todo: any check that the data dimensions are sane with feature_count with streaming_window?
    data = _flatten_data(data)
    data = _validate_numeric(data)
    data_csv = ','.join([str(float(d)) for d in data])

    url = _AMBER_URL + '/stream'
    headers = {
        'x-token': _amber_creds['api_key'],
        'api-tenant': _amber_creds['api_tenant'],
        'sensor-id': sensor_id
    }
    body = {
        'data': data_csv
    }
    return _api_call('POST', url, headers, body=body)


def train_sensor(sensor_id, data):
    """Trains an amber sensor using a given set of data

    Args:        
        sensor_id (str): sensor identifier
        data (array-like): data to be inferenced. Must be array-like in
            that it is a numeric scalar, list-like, or list-of-lists-like
            which has no side effects if iterated.
    
    Returns:
        succeess (bool): True if operation was successful
        response (str): amber server response
    """

    if not _amber_creds['is_set']:
        raise BoonException("credentials not set")

    # server expects data flattened as a string of comma-separated values
    # todo: any check that the data dimensions are sane with feature_count with streaming_window?
    data = _flatten_data(data)
    data = _validate_numeric(data)
    data_csv = ','.join([str(float(d)) for d in data])

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
    """Gets usage info about a sensor

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
    """Gets current sensor configuration

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
    """Gets sensor status

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
