from __future__ import absolute_import

import unittest
import os

from boonamber import (
    AmberV2Client,
    ApiException,
)
import boonamber

class TestData(unittest.TestCase):
    """Version unit test stubs"""

    def setUp(self):
        license_id = os.getenv('AMBER_TEST_LICENSE_ID')
        license_file = os.getenv('AMBER_TEST_LICENSE_FILE')
        self.api = AmberV2Client(license_id=license_id, license_file=license_file)
                
        self.model_id = "non-existant-id"

    def tearDown(self):
        pass

    def testPostDataNegative(self):
        """Test Post Data fail"""
        with self.assertRaises(ApiException):
            self.api.post_data(model_id=self.model_id, data="1,2,3", save_image=False)

        with self.assertRaises(ApiException):
            self.api.post_data(model_id=self.model_id, data=1, save_image=False)

    def testPutDataNegative(self):
        """Test Put Data fail"""
        v1 = boonamber.FusionFeature(name="feature-0", value=16)
        body = boonamber.PutDataRequest(vector=[v1])
        with self.assertRaises(ApiException):
            self.api.put_data(model_id=self.model_id, body=body)

    def testPostPretrainNegative(self):
        """Test Post Pretrain fail"""
        with self.assertRaises(ApiException):
            self.api.post_pretrain(model_id=self.model_id, data="1,2,3", block=True)

        # Test Post Pretrain data fail
        with self.assertRaises(ApiException):
            self.api.post_pretrain(model_id=self.model_id, data="none")

    def testGetPretrainNegative(self):
        """Test Get Pretrain fail"""
        with self.assertRaises(ApiException):
            self.api.get_pretrain(model_id=self.model_id)


if __name__ == '__main__':
    unittest.main()
