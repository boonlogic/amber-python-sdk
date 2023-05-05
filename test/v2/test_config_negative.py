from __future__ import absolute_import

import unittest
import os

from boonamber import (
    AmberV2Client,
    ApiException,
)
import boonamber

class TestConfig(unittest.TestCase):
    """Version unit test stubs"""

    def setUp(self):
        license_id = os.getenv('AMBER_TEST_LICENSE_ID')
        license_file = os.getenv('AMBER_TEST_LICENSE_FILE')
        self.api = AmberV2Client(license_id=license_id, license_file=license_file)

        self.model_id = "non-existant-id"

    def tearDown(self):
        pass

    def testPostConfigNegative(self):
        """Test Post Config fail"""
        features = boonamber.FeatureConfig(name="feature-0")
        configRequest = boonamber.PostConfigRequest(streaming_window=25, features=[features])
        with self.assertRaises(ApiException):
            self.api.post_config(model_id=self.model_id, body=configRequest)

    def testGetConfigNegative(self):
        """Test Get Config fail"""
        with self.assertRaises(ApiException):
            self.api.get_config(model_id=self.model_id)

    
if __name__ == '__main__':
    unittest.main()
