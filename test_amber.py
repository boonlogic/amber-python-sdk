import nose
from nose.tools import assert_equal
from nose.tools import assert_list_equal
from nose.tools import assert_dict_equal
from nose.tools import assert_false
from nose.tools import assert_raises
import boonamber as amber


class TestCredentials:
    def test_set_credentials
        raise NotImplementedError

    def test_set_credentials_negative
        # set credentials using non-string api_key
        raise NotImplementedError

        # set credentials using non-string api_tenant
        raise NotImplementedError


class TestEndpoints:
    def test_create_sensor
        raise NotImplementedError

    def test_create_sensor_negative
        # try with unset credentials
        raise NotImplementedError

        # try with garbage credentials
        raise NotImplementedError

        # try with already-created sensor-id
        raise NotImplementedError


    def test_delete_sensor
        raise NotImplementedError

    def test_delete_sensor_negative
        # try with unset credentials
        raise NotImplementedError

        # try with garbage credentials
        raise NotImplementedError

        # try with nonexistent sensor-id
        raise NotImplementedError


    def test_list_sensors
        raise NotImplementedError

    def test_list_sensors_negative
        # try with unset credentials
        raise NotImplementedError

        # try with garbage credentials
        raise NotImplementedError

    def test_configure_sensor
        raise NotImplementedError

    def test_configure_sensor_negative
        # try with unset credentials
        raise NotImplementedError

        # try with garbage credentials
        raise NotImplementedError

        # try with nonexistent sensor-id
        raise NotImplementedError

        # try with bad feature_count
        raise NotImplementedError

        # try with bad streaming_window
        raise NotImplementedError

    def test_stream_sensor
        raise NotImplementedError

    def test_stream_sensor_negative
        # try with unset credentials
        raise NotImplementedError

        # try with garbage credentials
        raise NotImplementedError

        # try with nonexistent sensor-id
        raise NotImplementedError

        # try with invalid data
        # bad_shape_data
        # nonnumeric_data
        raise NotImplementedError
        raise NotImplementedError

    def test_train_sensor
        raise NotImplementedError

    def test_train_sensor_negative
        # try with unset credentials
        raise NotImplementedError

        # try with garbage credentials
        raise NotImplementedError

        # try with nonexistent sensor-id
        raise NotImplementedError

        # try with invalid data
        # bad_shape_data
        # nonnumeric_data
        raise NotImplementedError
        raise NotImplementedError

    def test_get_info
        raise NotImplementedError

    def test_get_info_negative
        # try with unset credentials
        raise NotImplementedError

        # try with garbage credentials
        raise NotImplementedError

        # try with nonexistent sensor-id
        raise NotImplementedError

    def test_get_config
        raise NotImplementedError

    def test_get_config_negative
        # try with unset credentials
        raise NotImplementedError

        # try with garbage credentials
        raise NotImplementedError

        # try with nonexistent sensor-id
        raise NotImplementedError

    def test_get_status
        raise NotImplementedError

    def test_get_status_negative
        # try with unset credentials
        raise NotImplementedError

        # try with garbage credentials
        raise NotImplementedError

        # try with nonexistent sensor-id
        raise NotImplementedError


class TestAPICall:
    def test_api_call
        raise NotImplementedError

    def test_api_call_negative
        # try request with bad HTTP method
        raise NotImplementedError

        # try request with bad URL
        raise NotImplementedError

        # make a request that returns bad (non-200) error code
        raise NotImplementedError

        # make a request that returns backend error ('errorMessage' in response body)
        # todo: will this be possible for an end-user, or is it just a current error behavior of amber server?
        raise NotImplementedError


class TestDataHandling:
    def test_validate_shape
        # try with scalar
        raise NotImplementedError

        # try with list
        raise NotImplementedError

        # try with valid list-of-lists
        raise NotImplementedError

    def test_validate_shape_negative
        # try with empty data
        # empty_lists
        # empty_lists_of_lists
        raise NotImplementedError
        raise NotImplementedError

        # try with badly-nested data
        # mixed_nesting
        # too_deep
        # ragged_array
        raise NotImplementedError
        raise NotImplementedError
        raise NotImplementedError

    def test_flatten_data
        # flatten scalar
        raise NotImplementedError

        # flatten list
        raise NotImplementedError

        # flatten list-of-lists
        raise NotImplementedError

    def test_validate_numeric
        # try with (valid) list of numbers
        raise NotImplementedError

    def test_validate_numeric_negative
        # try with list containing non-number
        raise NotImplementedError


if __name__ == '__main__':
    myargv = ['nosetests', '--verbosity=2']
    nose.run(defaultTest=__name__ + ':TestCredentials', argv=myargv)
    nose.run(defaultTest=__name__ + ':TestAPICall', argv=myargv)
    nose.run(defaultTest=__name__ + ':TestDataHandling', argv=myargv)
    nose.run(defaultTest=__name__ + ':TestEndpoints', argv=myargv)
