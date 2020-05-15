###########################
# BoonAmber Python API v1 #
###########################


class BoonException(Exception):
    def __init__(self, message):
        self.message = message


def create_sensor(sensor_id, api_key, api_tenant):
    raise NotImplementedError


def delete_sensor(sensor_id, api_key, api_tenant):
    raise NotImplementedError


def list_sensors(api_key, api_tenant):
    raise NotImplementedError


def configure_sensor(sensor_id, feature_count, streaming_window, api_key, api_tenant):
    raise NotImplementedError


def get_config(sensor_id, api_key, api_tenant):
    raise NotImplementedError


def stream_sensor(sensor_id, api_key, api_tenant):
    raise NotImplementedError


def train_sensor(sensor_id, api_key, api_tenant):
    raise NotImplementedError


def get_info(sensor_id, api_key, api_tenant):
    raise NotImplementedError


def get_status(sensor_id, api_key, api_tenant):
    raise NotImplementedError
