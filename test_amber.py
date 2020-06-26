import nose
from nose.tools import assert_equal
from nose.tools import assert_true
from nose.tools import assert_raises
from nose.tools import assert_is_instance
from boonamber import AmberClient, BoonException


TEST_USER = 'amber-test-user'
TEST_PASSWORD = r'UFGdMzt*P1Zv*4%b'
TEST_SENSOR_ID = 'dca492f2b8a67697'


class TestAuth:
    def setUp(self):
        self.amber = AmberClient()

    def test_authenticate(self):
        # todo: make test user and fill in valid credentials
        success, response = self.amber.authenticate(TEST_USER, TEST_PASSWORD)
        assert_equal(success, True)

    def test_authenticate_negative(self):
        success, response = self.amber.authenticate('garbage-user', 'garbage-password')
        assert_equal(success, False)
        assert_true(response.startswith('401:'))

class TestEndpoints:
    def setUp(self):
        self.amber = AmberClient()
        self.amber.authenticate(TEST_USER, TEST_PASSWORD)

    def setup_unset_credentials(self):
        self.amber = AmberClient()

    def setup_expired_token(self):
        self.amber = AmberClient()
        self.amber.token = 'expired-token'

    def setup_created_sensor(self):
        success, sensor_id = self.amber.create_sensor('test-sensor')
        if not success:
            raise RuntimeError("setup failed")
        self.sensor_id = sensor_id

    def test_create_sensor(self):
        success, sensor_id = self.amber.create_sensor('test-sensor')
        assert_equal(success, True)

        success, response = self.amber.delete_sensor(sensor_id)
        if not success:
            raise RuntimeError("teardown failed, sensor was not deleted")

    def test_create_sensor_negative(self):
        self.setup_unset_credentials()
        assert_raises(BoonException, self.amber.create_sensor, 'test-sensor')

        self.setup_expired_token()
        success, response = self.amber.create_sensor('test-sensor')
        assert_equal(success, False)
        assert_true(response.startswith('401:'))

    def test_delete_sensor(self):
        self.setup_created_sensor()
        success, response = self.amber.delete_sensor(self.sensor_id)
        assert_equal(success, True)

    def test_delete_sensor_negative(self):
        self.setup_unset_credentials()
        assert_raises(BoonException, self.amber.delete_sensor, 'sensor-id-filler')

        self.setup_expired_token()
        success, response = self.amber.delete_sensor('sensor-id-filler')
        assert_equal(success, False)
        assert_true(response.startswith('401:'))

        # nonexistent sensor
        self.setUp()
        success, response = self.amber.delete_sensor('nonexistent-sensor-id')
        assert_equal(success, False)
        assert_true(response.startswith('404:'))

    def test_get_sensor(self):
        success, response = self.amber.get_sensor(TEST_SENSOR_ID)
        assert_equal(success, True)
        assert_true(response['sensor-id'] == TEST_SENSOR_ID)

    def test_get_sensor_negative(self):
        self.setup_unset_credentials()
        assert_raises(BoonException, self.amber.get_sensor, TEST_SENSOR_ID)

        self.setup_expired_token()
        success, response = self.amber.get_sensor(TEST_SENSOR_ID)
        assert_equal(success, False)
        assert_true(response.startswith('401:'))

        self.setUp()
        success, response = self.amber.get_sensor('nonexistent-sensor-id')
        assert_equal(success, False)
        assert_true(response.startswith('404:'))

    def test_list_sensors(self):
        success, response = self.amber.list_sensors()
        assert_equal(success, True)
        assert_true(TEST_SENSOR_ID in response.keys())

    def test_list_sensors_negative(self):
        self.setup_unset_credentials()
        assert_raises(BoonException, self.amber.list_sensors)

        self.setup_expired_token()
        success, response = self.amber.list_sensors()
        assert_equal(success, False)
        assert_true(response.startswith('401:'))

    def test_configure_sensor(self):
        expected_response = {
            'features': [{'maxVal': 1, 'minVal': 0}],
            'streamingWindowSize': 25,
            'enableAutoTuning': True,
            'samplesToBuffer': 10000,
            'learningGraduation': True,
            'learningRateNumerator': 10,
            'learningRateDenominator': 10000,
            'learningMaxClusters': 1000,
            'learningMaxSamples': 1000000,
            'percentVariation': 0.05
        }
        success, response = self.amber.configure_sensor(TEST_SENSOR_ID, features=1, streaming_window_size=25,
                                                        samples_to_buffer=10000,
                                                        learning_graduation=True,
                                                        learning_rate_numerator=10,
                                                        learning_rate_denominator=10000,
                                                        learning_max_clusters=1000,
                                                        learning_max_samples=1000000)
        assert_equal(success, True)
        assert_equal(response, expected_response)

    def test_configure_sensor_negative(self):
        self.setup_unset_credentials()
        assert_raises(BoonException, self.amber.configure_sensor, TEST_SENSOR_ID)

        self.setup_expired_token()
        success, response = self.amber.configure_sensor(TEST_SENSOR_ID)
        assert_equal(success, False)
        assert_true(response.startswith('401:'))

        self.setUp()
        success, response = self.amber.configure_sensor('nonexistent-sensor-id')
        assert_equal(success, False)
        assert_true(response.startswith('404:'))

        # invalid feature_count or streaming_window
        assert_raises(BoonException, self.amber.configure_sensor, TEST_SENSOR_ID, features=-1)
        assert_raises(BoonException, self.amber.configure_sensor, TEST_SENSOR_ID, features=1.5)
        assert_raises(BoonException, self.amber.configure_sensor, TEST_SENSOR_ID, streaming_window_size=-1)
        assert_raises(BoonException, self.amber.configure_sensor, TEST_SENSOR_ID, streaming_window_size=1.5)

    def test_get_config(self):
        expected_response = {
            'features': [{'maxVal': 1, 'minVal': 0}],
            'streamingWindowSize': 25,
            'enableAutoTuning': True,
            'samplesToBuffer': 10000,
            'learningGraduation': True,
            'learningRateNumerator': 10,
            'learningRateDenominator': 10000,
            'learningMaxClusters': 1000,
            'learningMaxSamples': 1000000,
            'percentVariation': 0.05
        }
        success, response = self.amber.get_config(TEST_SENSOR_ID)
        assert_equal(success, True)
        assert_equal(response, expected_response)

    def test_get_config_negative(self):
        self.setup_unset_credentials()
        assert_raises(BoonException, self.amber.get_config, TEST_SENSOR_ID)

        self.setup_expired_token()
        success, response = self.amber.get_config(TEST_SENSOR_ID)
        assert_equal(success, False)
        assert_true(response.startswith('401:'))

        self.setUp()
        success, response = self.amber.get_config('nonexistent-sensor-id')
        assert_equal(success, False)
        assert_true(response.startswith('404:'))

    def test_stream_sensor(self):
        # scalar data should return SI of length 1
        success, response = self.amber.stream_sensor(TEST_SENSOR_ID, 1)
        assert_equal(success, True)
        assert_true('state' in response)
        assert_true(len(response['SI']) == 1)

        # array data should return SI of same length
        success, response = self.amber.stream_sensor(TEST_SENSOR_ID, [1, 2, 3, 4, 5])
        assert_equal(success, True)
        assert_true('state' in response)
        assert_true(len(response['SI']) == 5)

    def test_stream_sensor_negative(self):
        self.setup_unset_credentials()
        assert_raises(BoonException, self.amber.stream_sensor, TEST_SENSOR_ID, [1, 2, 3, 4, 5])

        self.setup_expired_token()
        success, response = self.amber.stream_sensor(TEST_SENSOR_ID, [1, 2, 3, 4, 5])
        assert_equal(success, False)
        assert_true(response.startswith('401:'))

        self.setUp()
        success, response = self.amber.stream_sensor('nonexistent-sensor-id', [1, 2, 3, 4, 5])
        assert_equal(success, False)
        assert_true(response.startswith('404:'))

        # invalid data
        assert_raises(BoonException, self.amber.stream_sensor, TEST_SENSOR_ID, [])
        assert_raises(BoonException, self.amber.stream_sensor, TEST_SENSOR_ID, [1, '2', 3])
        assert_raises(BoonException, self.amber.stream_sensor, TEST_SENSOR_ID, [1, [2, 3], 4])

    def test_get_status(self):
        success, response = self.amber.get_config(TEST_SENSOR_ID)
        assert_equal(success, True)
        assert_is_instance(response, dict)

    def test_get_status_negative(self):
        self.setup_unset_credentials()
        assert_raises(BoonException, self.amber.get_config, TEST_SENSOR_ID)

        self.setup_expired_token()
        success, response = self.amber.get_config(TEST_SENSOR_ID)
        assert_equal(success, False)
        assert_true(response.startswith('401:'))

        self.setUp()
        success, response = self.amber.get_config('nonexistent-sensor-id')
        assert_equal(success, False)
        assert_true(response.startswith('404:'))


class TestAPICall:
    def setUp(self):
        self.amber = AmberClient()

        self.amber.authenticate(TEST_USER, TEST_PASSWORD)
        self.token = self.amber.token

        self.url = self.amber.url
        self.headers = {
            'Content-Type': 'application/json',
        }

    def test_api_call(self):
        self.headers['Authorization'] = 'Bearer {}'.format(self.token)
        success, response = self.amber._api_call('GET', self.url + '/sensors', self.headers)
        assert_equal(success, True)

    def test_api_call_negative(self):
        self.headers['Authorization'] = 'Bearer garbage-token'
        success, response = self.amber._api_call('GET', self.url + '/sensors', self.headers)
        assert_equal(success, False)
        assert_true(response.startswith("401:"))

        # todo: request that returns backend error ('errorMessage' in response body)
        # todo: how to reliably generate these?
        # raise NotImplementedError


class TestDataHandling:
    def setUp(self):
        self.amber = AmberClient()

    def test_convert_to_csv(self):
        # valid scalar inputs
        assert_equal("1.0", self.amber._convert_to_csv(1))
        assert_equal("1.0", self.amber._convert_to_csv(1.0))

        # valid 1d inputs
        assert_equal("1.0,2.0,3.0", self.amber._convert_to_csv([1, 2, 3]))
        assert_equal("1.0,2.0,3.0", self.amber._convert_to_csv([1, 2, 3.0]))
        assert_equal("1.0,2.0,3.0", self.amber._convert_to_csv([1.0, 2.0, 3.0]))

        # valid 2d inputs
        assert_equal("1.0,2.0,3.0,4.0", self.amber._convert_to_csv([[1, 2], [3, 4]]))
        assert_equal("1.0,2.0,3.0,4.0", self.amber._convert_to_csv([[1, 2, 3, 4]]))
        assert_equal("1.0,2.0,3.0,4.0", self.amber._convert_to_csv([[1], [2], [3], [4]]))
        assert_equal("1.0,2.0,3.0,4.0", self.amber._convert_to_csv([[1, 2], [3, 4.0]]))
        assert_equal("1.0,2.0,3.0,4.0", self.amber._convert_to_csv([[1.0, 2.0], [3.0, 4.0]]))

    def test_convert_to_csv_negative(self):
        # empty data
        assert_raises(ValueError, self.amber._convert_to_csv, [])
        assert_raises(ValueError, self.amber._convert_to_csv, [[]])
        assert_raises(ValueError, self.amber._convert_to_csv, [[], []])

        # non-numeric data
        assert_raises(ValueError, self.amber._convert_to_csv, None)
        assert_raises(ValueError, self.amber._convert_to_csv, 'a')
        assert_raises(ValueError, self.amber._convert_to_csv, 'abc')
        assert_raises(ValueError, self.amber._convert_to_csv, [1, None, 3])
        assert_raises(ValueError, self.amber._convert_to_csv, [1, 'a', 3])
        assert_raises(ValueError, self.amber._convert_to_csv, [1, 'abc', 3])
        assert_raises(ValueError, self.amber._convert_to_csv, [[1, None], [3, 4]])
        assert_raises(ValueError, self.amber._convert_to_csv, [[1, 'a'], [3, 4]])
        assert_raises(ValueError, self.amber._convert_to_csv, [[1, 'abc'], [3, 4]])

        # badly-shaped data
        assert_raises(ValueError, self.amber._convert_to_csv, [1, [2, 3], 4])            # mixed nesting
        assert_raises(ValueError, self.amber._convert_to_csv, [[1, 2], [3, 4, 5]])       # ragged array
        assert_raises(ValueError, self.amber._convert_to_csv, [[[1, 2, 3, 4]]])          # nested too deep
        assert_raises(ValueError, self.amber._convert_to_csv, [[[1], [2], [3], [4]]])


if __name__ == '__main__':
    argv = ['nosetests', '--verbosity=2']
    nose.run(defaultTest=__name__ + ':TestAuth', argv=argv)
    nose.run(defaultTest=__name__ + ':TestAPICall', argv=argv)
    nose.run(defaultTest=__name__ + ':TestDataHandling', argv=argv)
    nose.run(defaultTest=__name__ + ':TestEndpoints', argv=argv)
