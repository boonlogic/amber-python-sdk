from __future__ import absolute_import

import unittest
import csv
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
        self.api = AmberV2Client(license_id=license_id, license_file=license_file)
        
        self.label = "python:v2:tests-results"

        # create model
        postModels = boonamber.PostModelRequest(label=self.label)
        models = self.api.post_model(postModels)
        assert models.label == self.label
        self.model_id = models.id

        # configure model
        features = boonamber.FeatureConfig(name="feature-0")
        autotune = boonamber.Autotuning(percent_variation=False)
        training = boonamber.TrainingConfig(buffering_samples=400, learning_max_samples=500)
        configRequest = boonamber.PostConfigRequest(streaming_window=25, features=[features], training=training, autotuning=autotune)
        self.config = self.api.post_config(model_id=self.model_id, body=configRequest)
        assert round(self.config.percent_variation, 2) == 0.05
        
        # populate some of the model
        with open("output_current.csv", 'r') as f:
            csv_reader = csv.reader(f, delimiter=',')
            data = [str(d) for row in csv_reader for d in row]
        data = data[:500]
        assert len(data) == 500
        data = ",".join(data)

        response = self.api.post_data(model_id=self.model_id, data=data, save_image=False)
        assert response.status.state == "Monitoring"

    def tearDown(self):
        # delete test model
        self.api.delete_model(self.model_id)

    def testPostLearning(self):
        """Test Post Learning"""
        training = boonamber.TrainingConfig(buffering_samples=400, learning_max_samples=500)
        response = self.api.enable_learning(model_id=self.model_id, training=training)
        assert "Learning" == response.status.state

    def testGetNanoStatus(self):
        """Test Get Nano Status"""
        response = self.api.get_nano_status(model_id=self.model_id)
        assert response.state == "Monitoring"
        assert response.cluster_count == 59
        assert response.sample_count == 476

    def testGetStatus(self):
        """Test Get Status"""
        response = self.api.get_status(model_id=self.model_id)
        assert response.state == "Monitoring"
        assert response.cluster_count == 59
        assert response.sample_count == 476

    def testGetDiagnostic(self):
        """Test Get Diagnostic"""
        path = self.api.get_diagnostic(model_id=self.model_id, dir=os.getcwd())
        assert os.path.exists(path)

        os.remove(path)

    def testGetRootCause(self):
        """Test Get Root Cause"""
        response = self.api.get_root_cause(model_id=self.model_id, clusters=1)
        assert len(response.root_cause_list) == 1

        response = self.api.get_root_cause(model_id=self.model_id, clusters=[1,2])
        assert len(response.root_cause_list) == 2

        response = self.api.get_root_cause(model_id=self.model_id, clusters="1")
        assert len(response.root_cause_list) == 1

        response = self.api.get_root_cause(model_id=self.model_id, clusters="1,2,3")
        assert len(response.root_cause_list) == 3

        with self.assertRaises(ApiException) as exp:
            self.api.get_root_cause(model_id=self.model_id, clusters="[1,2]")
        assert 'must specify cluster ID(s) in the format' in str(exp.exception)

        response = self.api.get_root_cause(model_id=self.model_id, vectors=[1]*25)
        assert len(response.root_cause_list) == 1

        response = self.api.get_root_cause(model_id=self.model_id, vectors=[[1]*25, [0.5]*25])
        assert len(response.root_cause_list) == 2

        with self.assertRaises(ApiException) as exp:
            self.api.get_root_cause(model_id=self.model_id, vectors="[{}]".format(",".join(["1"]*25)))
        assert 'must specify patterns(s) in the format' in str(exp.exception)

    def testPostOutage(self):
        """Test Post Outage"""
        self.api.post_outage(model_id=self.model_id)

        # test state
        response = self.api.get_status(model_id=self.model_id)
        assert response.state == "Monitoring"
        assert response.cluster_count == 59
        assert response.sample_count == 476


if __name__ == '__main__':
    unittest.main()
