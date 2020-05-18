import nose
from nose.tools import assert_equal
from nose.tools import assert_true
from nose.tools import assert_raises
from nose.tools import assert_is_instance
import boonamber as amber


# sensor-id reserved for testing -- is created and destroyed during tests
TEST_SENSOR = 'my-test-sensor'


class TestCredentials:
    def setUp(self):
        # un-set credentials
        amber._amber_creds['api_key'] = None
        amber._amber_creds['api_tenant'] = None
        amber._amber_creds['is_set'] = False

    def test_set_credentials(self):
        amber.set_credentials(api_key='api-key', api_tenant='api-tenant')
        assert_equal(amber._amber_creds['api_key'], 'api-key')
        assert_equal(amber._amber_creds['api_tenant'], 'api-tenant')

    def test_set_credentials_negative(self):
        # non-string api_key or api_tenant
        assert_raises(amber.BoonException, amber.set_credentials, api_key=None, api_tenant='api-tenant')
        assert_raises(amber.BoonException, amber.set_credentials, api_key=12345, api_tenant='api-tenant')
        assert_raises(amber.BoonException, amber.set_credentials, api_key='api-key', api_tenant=None)
        assert_raises(amber.BoonException, amber.set_credentials, api_key='api-key', api_tenant=12345)


class TestEndpoints:
    def setUp(self):
        amber.set_credentials(api_key='api-key', api_tenant='api-tenant')
        success, current_sensors = amber.list_sensors()
        if not success:
            raise RuntimeError("setup failed")

        if TEST_SENSOR in current_sensors:
            success, response = amber.delete_sensor(TEST_SENSOR)
            if not success:
                raise RuntimeError("setup failed")

        success, response = amber.create_sensor(TEST_SENSOR)
        if not success:
            raise RuntimeError("setup failed")

    def setup_unset_credentials(self):
        amber._amber_creds['api_key'] = None
        amber._amber_creds['api_tenant'] = None
        amber._amber_creds['is_set'] = False

    def setup_garbage_credentials(self):
        amber.set_credentials(api_key='garbage-credential', api_tenant='garbage-credential')

    def setup_nonexistent_sensor(self):
        amber.set_credentials(api_key='api-key', api_tenant='api-tenant')
        success, current_sensors = amber.list_sensors()
        if not success:
            raise RuntimeError("setup failed")

        if TEST_SENSOR in current_sensors:
            success, response = amber.delete_sensor(TEST_SENSOR)
            if not success:
                raise RuntimeError("setup failed")

    def test_create_sensor(self):
        self.setup_uncreated()
        success, response = amber.create_sensor(TEST_SENSOR)
        assert_equal(success, True)
        assert_equal(response, "sensor created")

    def test_create_sensor_negative(self):
        self.setup_unset_credentials()
        assert_raises(amber.BoonException, amber.create_sensor, TEST_SENSOR)

        self.setup_garbage_credentials()
        success, response = amber.create_sensor(TEST_SENSOR)
        assert_equal(success, False)
        assert_true(response.startswith('401:'))

        self.setUp()
        success, response = amber.create_sensor(TEST_SENSOR)
        assert_equal(success, False)
        assert_true(response.startswith('400:'))

    def test_delete_sensor(self):
        success, response = amber.delete_sensor(TEST_SENSOR)
        assert_equal(success, True)
        assert_equal(response, "sensor deleted")

    def test_delete_sensor_negative(self):
        self.setup_unset_credentials()
        assert_raises(amber.BoonException, amber.delete_sensor, TEST_SENSOR)

        self.setup_garbage_credentials()
        success, response = amber.delete_sensor(TEST_SENSOR)
        assert_equal(success, False)
        assert_true(response.startswith('401:'))

        self.setup_nonexistent_sensor(TEST_SENSOR)
        success, response = amber.delete_sensor(TEST_SENSOR)
        assert_equal(success, False)
        assert_true(response.startswith('404:'))

    def test_list_sensors(self):
        success, response = amber.list_sensors()
        assert_equal(success, True)
        assert_is_instance(response, list)

    def test_list_sensors_negative(self):
        self.setup_unset_credentials()
        assert_raises(amber.BoonException, amber.list_sensors)

        self.setup_garbage_credentials()
        success, response = amber.list_sensors()
        assert_equal(success, False)
        assert_true(response.startswith('401:'))

    def test_configure_sensor(self):
        target_response = {
            'accuracy': 0.99,
            'features': [
                {
                    'minVal': 0,
                    'maxVal': 1,
                    'weight': 1
                }
            ],
            'numericFormat': 'float32',
            'percentVariation': 0.05,
            'streamingWindowSize': 25,
        }
        success, response = amber.configure_sensor(TEST_SENSOR, feature_count=1, streaming_window=25)
        assert_equal(success, True)
        assert_dict_equal(response.json(), target_response)
        success, response = amber.configure_sensor(TEST_SENSOR, feature_count=1.0, streaming_window=25.0)
        assert_equal(success, True)
        assert_dict_equal(response.json(), target_response)

    def test_configure_sensor_negative(self):
        self.setup_unset_credentials()
        assert_raises(amber.BoonException, amber.configure_sensor, TEST_SENSOR)

        self.setup_garbage_credentials()
        assert_raises(amber.BoonException, amber.configure_sensor, TEST_SENSOR)

        self.setup_nonexistent_sensor()
        success, response = amber.configure_sensor(TEST_SENSOR)
        assert_equal(success, False)
        assert_true(response.startswith('404:'))

        # invalid feature_count or streaming_window
        assert_raises(amber.BoonException, amber.configure_sensor, TEST_SENSOR, feature_count=-1)
        assert_raises(amber.BoonException, amber.configure_sensor, TEST_SENSOR, feature_count=1.5)
        assert_raises(amber.BoonException, amber.configure_sensor, TEST_SENSOR, streaming_window=-1)
        assert_raises(amber.BoonException, amber.configure_sensor, TEST_SENSOR, streaming_window=1.5)

    def test_stream_sensor(self):
        # scalar data should return scalar result
        success, response = amber.stream_sensor(TEST_SENSOR, 1)
        assert_equal(success, True)
        assert_is_instance(response, float)

        # array data should return result of same length
        success, response = amber.stream_sensor(TEST_SENSOR, [1, 2, 3, 4, 5])
        assert_equal(success, True)
        assert_true(len(response) == 5)

    def test_stream_sensor_negative(self):
        self.setup_unset_credentials()
        assert_raises(amber.BoonException, amber.stream_sensor, TEST_SENSOR, [1, 2, 3, 4, 5])

        self.setup_garbage_credentials()
        assert_raises(amber.BoonException, amber.stream_sensor, TEST_SENSOR, [1, 2, 3, 4, 5])

        self.setup_nonexistent_sensor()
        success, response = amber.stream_sensor(TEST_SENSOR, [1, 2, 3, 4, 5])
        assert_equal(success, False)
        assert_true(response.startswith('404:'))

        # invalid data
        assert_raises(amber.BoonException, amber.stream_sensor, TEST_SENSOR, [])
        assert_raises(amber.BoonException, amber.stream_sensor, TEST_SENSOR, [1, '2', 3])
        assert_raises(amber.BoonException, amber.stream_sensor, TEST_SENSOR, [1, [2, 3], 4])

    # def test_train_sensor(self):
    #     # todo: what will response look like?
    #     success, response = amber.train_sensor(TEST_SENSOR, [1, 2, 3, 4, 5])
    #     assert_equal(success, True)
    #     assert_equal(response, "train successful")

    def test_train_sensor_negative(self):
        self.setup_unset_credentials()
        assert_raises(amber.BoonException, amber.train_sensor, TEST_SENSOR, [1, 2, 3, 4, 5])

        self.setup_garbage_credentials()
        assert_raises(amber.BoonException, amber.train_sensor, TEST_SENSOR, [1, 2, 3, 4, 5])

        self.setup_nonexistent_sensor()
        success, response = amber.train_sensor(TEST_SENSOR, [1, 2, 3, 4, 5])
        assert_equal(success, False)
        assert_true(response.startswith('404:'))

        # invalid data
        assert_raises(amber.BoonException, amber.train_sensor, TEST_SENSOR, [])
        assert_raises(amber.BoonException, amber.train_sensor, TEST_SENSOR, [1, '2', 3])
        assert_raises(amber.BoonException, amber.train_sensor, TEST_SENSOR, [1, [2, 3], 4])

    # def test_get_info(self):
    #     # todo: more stringent check once response is better defined
    #     success, response = amber.get_info(TEST_SENSOR)
    #     assert_equal(success, True)
    #     assert_true('sensor-id' in response)

    def test_get_info_negative(self):
        self.setup_unset_credentials()
        assert_raises(amber.BoonException, amber.get_info, TEST_SENSOR)

        self.setup_garbage_credentials()
        success, response = amber.get_info(TEST_SENSOR)
        assert_equal(success, False)
        assert_true(response.startswith('401:'))

        self.setup_nonexistent_sensor(TEST_SENSOR)
        success, response = amber.get_info(TEST_SENSOR)
        assert_equal(success, False)
        assert_true(response.startswith('404:'))

    # def test_get_config(self):
    #     # todo: more stringent check once response is better defined
    #     success, response = amber.get_config(TEST_SENSOR)
    #     assert_equal(success, True)
    #     assert_is_instance(response, dict)

    def test_get_config_negative(self):
        self.setup_unset_credentials()
        assert_raises(amber.BoonException, amber.get_config, TEST_SENSOR)

        self.setup_garbage_credentials()
        success, response = amber.get_config(TEST_SENSOR)
        assert_equal(success, False)
        assert_true(response.startswith('401:'))

        self.setup_nonexistent_sensor(TEST_SENSOR)
        success, response = amber.get_config(TEST_SENSOR)
        assert_equal(success, False)
        assert_true(response.startswith('404:'))

    # def test_get_status(self):
    #     # todo: more stringent check once response is better defined
    #     success, response = amber.get_config(TEST_SENSOR)
    #     assert_equal(success, True)
    #     assert_is_instance(response, dict)

    def test_get_status_negative(self):
        self.setup_unset_credentials()
        assert_raises(amber.BoonException, amber.get_config, TEST_SENSOR)

        self.setup_garbage_credentials()
        success, response = amber.get_config(TEST_SENSOR)
        assert_equal(success, False)
        assert_true(response.startswith('401:'))

        self.setup_nonexistent_sensor(TEST_SENSOR)
        success, response = amber.get_config(TEST_SENSOR)
        assert_equal(success, False)
        assert_true(response.startswith('404:'))


class TestAPICall:
    def setUp(self):
        self.headers = {
            'x-token': 'api-key',
            'api-tenant': 'api-tenant',
        }

    def test_api_call(self):
        success, response = amber._api_call('GET', amber._AMBER_URL + '/sensors', self.headers)
        assert_equal(success, True)

    def test_api_call_negative(self):
        success, response = amber._api_call('GET', 'BADURL', self.headers)
        assert_equal(success, False)
        assert_true(response.startswith("request failed:"))

        # todo: request that returns bad (non-200) error code
        # raise NotImplementedError

        # todo: request that returns backend error ('errorMessage' in response body)
        # todo: is this just a current error behavior of amber server?
        # raise NotImplementedError


class TestDataHandling:
    def test_convert_to_csv(self):
        # valid scalar inputs
        assert_equal("1.0", amber._convert_to_csv(1))
        assert_equal("1.0", amber._convert_to_csv(1.0))

        # valid 1d inputs
        assert_equal("1.0,2.0,3.0", amber._convert_to_csv([1, 2, 3]))
        assert_equal("1.0,2.0,3.0", amber._convert_to_csv([1, 2, 3.0]))
        assert_equal("1.0,2.0,3.0", amber._convert_to_csv([1.0, 2.0, 3.0]))

        # valid 2d inputs
        assert_equal("1.0,2.0,3.0,4.0", amber._convert_to_csv([[1, 2], [3, 4]]))
        assert_equal("1.0,2.0,3.0,4.0", amber._convert_to_csv([[1, 2, 3, 4]]))
        assert_equal("1.0,2.0,3.0,4.0", amber._convert_to_csv([[1], [2], [3], [4]]))
        assert_equal("1.0,2.0,3.0,4.0", amber._convert_to_csv([[1, 2], [3, 4.0]]))
        assert_equal("1.0,2.0,3.0,4.0", amber._convert_to_csv([[1.0, 2.0], [3.0, 4.0]]))

    def test_convert_to_csv_negative(self):
        # empty data
        assert_raises(ValueError, amber._convert_to_csv, [])
        assert_raises(ValueError, amber._convert_to_csv, [[]])
        assert_raises(ValueError, amber._convert_to_csv, [[], []])

        # non-numeric data
        assert_raises(ValueError, amber._convert_to_csv, None)
        assert_raises(ValueError, amber._convert_to_csv, 'a')
        assert_raises(ValueError, amber._convert_to_csv, 'abc')
        assert_raises(ValueError, amber._convert_to_csv, [1, None, 3])
        assert_raises(ValueError, amber._convert_to_csv, [1, 'a', 3])
        assert_raises(ValueError, amber._convert_to_csv, [1, 'abc', 3])
        assert_raises(ValueError, amber._convert_to_csv, [[1, None], [3, 4]])
        assert_raises(ValueError, amber._convert_to_csv, [[1, 'a'], [3, 4]])
        assert_raises(ValueError, amber._convert_to_csv, [[1, 'abc'], [3, 4]])

        # badly-shaped data
        assert_raises(ValueError, amber._convert_to_csv, [1, [2, 3], 4])            # mixed nesting
        assert_raises(ValueError, amber._convert_to_csv, [[1, 2], [3, 4, 5]])       # ragged array
        assert_raises(ValueError, amber._convert_to_csv, [[[1, 2, 3, 4]]])          # nested too deep
        assert_raises(ValueError, amber._convert_to_csv, [[[1], [2], [3], [4]]])


if __name__ == '__main__':
    myargv = ['nosetests', '--verbosity=2']
    nose.run(defaultTest=__name__ + ':TestCredentials', argv=myargv)
    # nose.run(defaultTest=__name__ + ':TestAPICall', argv=myargv)
    nose.run(defaultTest=__name__ + ':TestDataHandling', argv=myargv)
    # nose.run(defaultTest=__name__ + ':TestEndpoints', argv=myargv)
