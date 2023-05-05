from __future__ import absolute_import

import unittest
import os

from boonamber import (
    AmberV2Client,
    ApiException,
)
import boonamber

class TestModels(unittest.TestCase):
    """Version unit test stubs"""

    def setUp(self):
        license_id = os.getenv('AMBER_TEST_LICENSE_ID')
        license_file = os.getenv('AMBER_TEST_LICENSE_FILE')
        self.api = AmberV2Client(license_id=license_id, license_file=license_file)
        
        self.model_id = "non-existant-id"
        self.label = "python:v2:tests"

    def tearDown(self):
        pass

    # def testPostModels(self):
    #     """Test Post Models"""
    #     postModels = boonamber.PostModelRequest(label=self.label)
    #     with self.assertRaises(ApiException):
    #         models = self.api.post_model(postModels)

    # def testGetModels(self):
    #     """Test Get Models"""
    #     models = self.api.get_models().to_dict()["model_list"]
    #     assert self.model_id in [m["id"] for m in models]

    def testGetModelNegative(self):
        """Test Get Model fail"""
        with self.assertRaises(ApiException):
            self.api.get_model(self.model_id)

    def testPutModelNegative(self):
        """Test Put Model fail"""
        metadata = boonamber.PutModelRequest(label="{}-update".format(self.label))
        with self.assertRaises(ApiException):
            self.api.put_model(self.model_id, metadata)

    def testDeleteModelNegative(self):
        """Test Delete Model fail"""
        with self.assertRaises(ApiException):
            self.api.delete_model(self.model_id)


if __name__ == '__main__':
    unittest.main()
