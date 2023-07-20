from __future__ import absolute_import

import unittest
import time
import csv
import os

from boonamber import (
    AmberV2Client,
)
import boonamber

class TestData(unittest.TestCase):
    """Version unit test stubs"""

    def setUp(self):
        license_id = os.getenv('AMBER_TEST_LICENSE_ID')
        license_file = os.getenv('AMBER_TEST_LICENSE_FILE')
        self.api = AmberV2Client.from_license_file(license_id=license_id, license_file=license_file)
        
        self.label = "python:v2:tests-streaming"

        # create model
        postModels = boonamber.PostModelRequest(label=self.label)
        models = self.api.post_model(postModels)
        assert models.label == self.label
        self.model_id = models.id

        # configure model
        features = boonamber.FeatureConfig(name="feature-0")
        training = boonamber.TrainingConfig(buffering_samples=500)
        autotune = boonamber.AutotuneConfig(percent_variation=False)
        configRequest = boonamber.PostConfigRequest(streaming_window=25, features=[features],
                                                   training=training, autotuning=autotune)
        config = self.api.post_config(model_id=self.model_id, body=configRequest)
        assert round(config.percent_variation, 2) == 0.05

    def tearDown(self):
        # delete test model
        self.api.delete_model(self.model_id)

    def testPostData(self):
        """Test Post Data"""
        # load file
        with open("output_current.csv", 'r') as f:
            csv_reader = csv.reader(f, delimiter=',')
            data = [str(d) for row in csv_reader for d in row]
        data = data[:600]
        assert len(data) == 600

        # test data
        response = self.api.post_data(model_id=self.model_id, data=data, save_image=False)
        assert "Learning" == response.status.state

        # test data string
        data = ",".join(data)
        response = self.api.post_data(model_id=self.model_id, data=data, save_image=False)
        assert "Learning" == response.status.state

    def testPutData(self):
        """Test Put Data"""
        v1 = boonamber.FusionFeature(name="feature-0", value=16)
        body = boonamber.PutDataRequest(vector=[v1])
        response = self.api.put_data(model_id=self.model_id, body=body)
        assert "Buffering" == response.status.state

    def testPostPretrain(self):
        """Test Post Pretrain"""
        # load file
        with open("output_current.csv", 'r') as f:
            csv_reader = csv.reader(f, delimiter=',')
            data = [str(d) for row in csv_reader for d in row]
        data = data[:500]
        assert len(data) == 500
        data = ",".join(data)

        # test pretrain
        response = self.api.post_pretrain(model_id=self.model_id, data=data, block=True)
        assert response.status == "Pretrained"

        response = self.api.post_pretrain(model_id=self.model_id, data=data, block=False)
        assert response.status == "Pretrained" or response.status == "Pretraining"

        while response.status == "Pretraining":
            time.sleep(3)
            response = self.api.get_pretrain(model_id=self.model_id)

    def testGetPretrain(self):
        """Test Get Pretrain"""
        response = self.api.get_pretrain(model_id=self.model_id)
        assert "None" == response.status


if __name__ == '__main__':
    unittest.main()
