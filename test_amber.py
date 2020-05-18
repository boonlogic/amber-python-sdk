import nose
from nose.tools import assert_equal
from nose.tools import assert_true
from nose.tools import assert_raises
from nose.tools import assert_is_instance
import boonamber as amber


class TestCredentials:
    def setUp(self):
        # unset credentials
        amber._amber_creds['api_key'] = None
        amber._amber_creds['api_tenant'] = None
        amber._amber_creds['is_set'] = False

    def test_set_credentials(self):
        amber.set_credentials(api_key='api-key', api_tenant='api-tenant')
        assert_equal(amber._amber_creds['api_key'], 'api-key')
        assert_equal(amber._amber_creds['api_tenant'], 'api-tenant')

    def test_set_credentials_negative(self):
        # set credentials using non-string api_key
        assert_raises(amber.BoonException, amber.set_credentials, api_key=None, api_tenant='api-tenant')

        # set credentials using non-string api_tenant
        assert_raises(amber.BoonException, amber.set_credentials, api_key='api-key', api_tenant=None)


class TestEndpoints:
    def test_create_sensor(self):
        raise NotImplementedError

    def test_create_sensor_negative(self):
        # try with unset credentials
        raise NotImplementedError

        # try with garbage credentials
        raise NotImplementedError

        # try with already-created sensor-id
        raise NotImplementedError


    def test_delete_sensor(self):
        raise NotImplementedError

    def test_delete_sensor_negative(self):
        # try with unset credentials
        raise NotImplementedError

        # try with garbage credentials
        raise NotImplementedError

        # try with nonexistent sensor-id
        raise NotImplementedError


    def test_list_sensors(self):
        raise NotImplementedError

    def test_list_sensors_negative(self):
        # try with unset credentials
        raise NotImplementedError

        # try with garbage credentials
        raise NotImplementedError

    def test_configure_sensor(self):
        raise NotImplementedError

    def test_configure_sensor_negative(self):
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

    def test_stream_sensor(self):
        raise NotImplementedError

    def test_stream_sensor_negative(self):
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

    def test_train_sensor(self):
        raise NotImplementedError

    def test_train_sensor_negative(self):
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

    def test_get_info(self):
        raise NotImplementedError

    def test_get_info_negative(self):
        # try with unset credentials
        raise NotImplementedError

        # try with garbage credentials
        raise NotImplementedError

        # try with nonexistent sensor-id
        raise NotImplementedError

    def test_get_config(self):
        raise NotImplementedError

    def test_get_config_negative(self):
        # try with unset credentials
        raise NotImplementedError

        # try with garbage credentials
        raise NotImplementedError

        # try with nonexistent sensor-id
        raise NotImplementedError

    def test_get_status(self):
        raise NotImplementedError

    def test_get_status_negative(self):
        # try with unset credentials
        raise NotImplementedError

        # try with garbage credentials
        raise NotImplementedError

        # try with nonexistent sensor-id
        raise NotImplementedError


class TestAPICall:
    def setUp(self):
        self.headers = {
            'x-token': 'api-key',
            'api-tenant': 'api-tenant',
        }

    def test_api_call(self):
        success, response = amber._api_call('GET', amber._AMBER_URL + '/sensors', self.headers)
        assert_equal(success, True)
        assert_is_instance(response, list)

    def test_api_call_negative(self):
        # try request with garbage URL
        success, response = amber._api_call('GET', 'BADURL', self.headers)
        assert_equal(success, False)
        assert_true(response.startswith("request failed:"))

        # make a request that returns bad (non-200) error code
        raise NotImplementedError

        # make a request that returns backend error ('errorMessage' in response body)
        # todo: will this be possible for an end-user, or is it just a current error behavior of amber server?
        raise NotImplementedError


class TestDataHandling:
    def test_validate_shape(self):
        # try with scalar
        amber._validate_shape(1)

        # try with list
        amber._validate_shape([1, 2, 3])

        # try with valid list-of-lists
        amber._validate_shape([[1, 2], [3, 4]])

    def test_validate_shape_negative(self):
        # try with empty data
        empty_1d = []
        empty_2d = [[], []]
        assert_raises(ValueError, amber._validate_shape, empty_1d)
        assert_raises(ValueError, amber._validate_shape, empty_2d)

        # try with badly-nested data
        mixed_nesting = [1, [2, 3], 4]
        too_deep = [[[1], [2]], [[3], [4]]]
        ragged_array = [[1, 2], [3, 4, 5]]
        assert_raises(ValueError, amber._validate_shape, mixed_nesting)
        assert_raises(ValueError, amber._validate_shape, too_deep)
        assert_raises(ValueError, amber._validate_shape, ragged_array)

    def test_flatten_data(self):
        # try with scalar
        flattened = amber._flatten_data(1)
        assert_equal(flattened, [1])

        # try with list
        flattened = amber._flatten_data([1, 2, 3])
        assert_equal(flattened, [1, 2, 3])

        # try with list-of-lists
        flattened = amber._flatten_data([[1, 2], [3, 4]])
        assert_equal(flattened, [1, 2, 3, 4])

    def test_validate_numeric(self):
        # try with (valid) list of numbers
        amber._validate_numeric([1, 2, 3])
        amber._validate_numeric([1, 2, 3.0])
        amber._validate_numeric([1.0, 2.0, 3.0])

    def test_validate_numeric_negative(self):
        # try with list containing non-number
        assert_raises(ValueError, amber._validate_shape, [1, '2', 3])


if __name__ == '__main__':
    myargv = ['nosetests', '--verbosity=2']
    nose.run(defaultTest=__name__ + ':TestCredentials', argv=myargv)
    # nose.run(defaultTest=__name__ + ':TestAPICall', argv=myargv)
    nose.run(defaultTest=__name__ + ':TestDataHandling', argv=myargv)
    # nose.run(defaultTest=__name__ + ':TestEndpoints', argv=myargv)
