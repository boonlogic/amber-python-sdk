from __future__ import absolute_import

import unittest
import os

from boonamber import (
    AmberV2Client,
    ApiException,
)
import boonamber

class TestResults(unittest.TestCase):
    """Version unit test stubs"""

    def setUp(self):
        license_id = os.getenv('AMBER_TEST_LICENSE_ID')
        license_file = os.getenv('AMBER_TEST_LICENSE_FILE')
        self.api = AmberV2Client(profile_name=license_id, license_file=license_file)

        self.model_id = "non-existant-id"

    def tearDown(self):
        pass

    def testPostLearningNegative(self):
        """Test Post Learning fail"""
        with self.assertRaises(ApiException):
            training = boonamber.TrainingConfig(buffering_samples=100, learning_max_samples=100)
            learning = boonamber.PostLearningRequest(state="Learning", training=training)
            self.api.enable_learning(model_id=self.model_id, body=learning)

    def testGetNanoStatusNegative(self):
        """Test Get Nano Status fail"""
        with self.assertRaises(ApiException):
            self.api.get_nano_status(model_id=self.model_id)
        
    def testGetStatusNegative(self):
        """Test Get Status fail"""
        with self.assertRaises(ApiException):
            self.api.get_status(model_id=self.model_id)

    def testGetDiagnosticNegative(self):
        """Test Get Diagnostic fail"""
        with self.assertRaises(ApiException) as exp:
            self.api.get_diagnostic(model_id=self.model_id, dir="bogus/path")
        assert 'target directory does not exist' in str(exp.exception)

    def testGetRootCauseNegative(self):
        """Test Get Root Cause fail"""
        with self.assertRaises(ApiException):
            self.api.get_root_cause(model_id=self.model_id, clusters="1,2")

        with self.assertRaises(ApiException):
            self.api.get_root_cause(model_id=self.model_id, clusters=[[[1]]])

        with self.assertRaises(ApiException):
            self.api.get_root_cause(model_id=self.model_id, clusters=boonamber.GetRootCauseResponse())

        with self.assertRaises(ApiException):
            self.api.get_root_cause(model_id=self.model_id, vectors=[[[1]]])

        with self.assertRaises(ApiException):
            self.api.get_root_cause(model_id=self.model_id, vectors=boonamber.GetRootCauseResponse())

    def testPostOutageNegative(self):
        """Test Post Outage fail"""
        with self.assertRaises(ApiException):
            self.api.post_outage(model_id=self.model_id)


if __name__ == '__main__':
    unittest.main()
