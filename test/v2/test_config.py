from __future__ import absolute_import

import unittest

import boonamber
from test.v2.create_test_client import create_test_client

class TestConfig(unittest.TestCase):
    """Version unit test stubs"""

    def setUp(self):
        self.api = create_test_client()
        self.label = "python:v2:tests-config"

        # create model
        postModels = boonamber.PostModelRequest(label=self.label)
        models = self.api.post_model(postModels)
        assert models.label == self.label
        self.model_id = models.id

    def tearDown(self):
        # delete test model
        self.api.delete_model(self.model_id)

    def testPostConfig(self):
        """Test Post Config"""
        config = self.api.post_config(model_id=self.model_id,
                                      body=boonamber.PostConfigRequest(streaming_window=25,
                                                                       features=[boonamber.FeatureConfig()]))
        assert round(config.percent_variation, 2) == 0.05
        assert len(config.features) == 1

    def testGetConfig(self):
        """Test Get Config"""
        features = boonamber.FeatureConfig(name="feature-0")
        configRequest = boonamber.PostConfigRequest(streaming_window=25, features=[features])
        config = self.api.post_config(model_id=self.model_id, body=configRequest)

        # test get config
        config = self.api.get_config(model_id=self.model_id)
        assert round(config.percent_variation, 2) == 0.05


if __name__ == '__main__':
    unittest.main()
