import requests


###########################
# BoonAmber Python API v1 #
###########################


_AMBER_URL = "https://yr15pccsn4.execute-api.us-east-1.amazonaws.com/dev-python"
_amber_creds = {'api_key': None,
                'api_tenant': None,
                'is_set': False}


class BoonException(Exception):
    def __init__(self, message):
        self.message = message


def _api_call(method, url, headers, data=None):
    response = requests.request(method=method, url=url, headers=headers, data=data)

    if response.status_code != 200:
        return False, '{}: {}'.format(response.status_code, response.json()['body'])

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
    """Creates a new sensor instance
    
    Args:
        sensor_id (str): sensor identifier
    """
    if not _amber_creds['is_set']:
        return False, "credentials not set"

    url = _AMBER_URL + '/sensor'
    headers = {
        'x-token': _amber_creds['api_key'],
        'api-tenant': _amber_creds['api_tenant'],
        'sensor-id': sensor_id
    }
    return _api_call('POST', url, headers)


def delete_sensor(sensor_id):
    raise NotImplementedError


def list_sensors():
    raise NotImplementedError


def configure_sensor(sensor_id, feature_count, streaming_window):
    raise NotImplementedError


def get_config(sensor_id):
    raise NotImplementedError


def stream_sensor(sensor_id):
    raise NotImplementedError


def train_sensor(sensor_id):
    raise NotImplementedError


def get_info(sensor_id):
    raise NotImplementedError


def get_status(sensor_id):
    raise NotImplementedError
