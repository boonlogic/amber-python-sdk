from __future__ import absolute_import

import unittest

from test.v2.create_test_client import create_test_client

import boonamber

class TestModels(unittest.TestCase):
    """Version unit test stubs"""

    def setUp(self):
        self.api = create_test_client()
        self.label = "python:v2:tests-models"

        # TODO: JAT, get migrate testing working
        #license_id = os.getenv('AMBER_V1_LICENSE_ID')
        #self.v1 = AmberClient(license_id=license_id, license_file=license_file)
        
        # create model
        postModels = boonamber.PostModelRequest(label=self.label)
        models = self.api.post_model(postModels)
        assert models.label == self.label
        self.model_id = models.id

    def tearDown(self):
        # delete test model
        self.api.delete_model(self.model_id)

    def testPostModels(self):
        """Test Post Models"""
        postModels = boonamber.PostModelRequest(label=self.label)
        models = self.api.post_model(postModels)
        assert models.label == self.label

        self.api.delete_model(models.id)

    def testPostModelCopy(self):
        """Test Post Model Copy"""
        response = self.api.copy_model(self.model_id)
        assert response.label == self.label

        # clean up
        self.api.delete_model(response.id)

        response = self.api.copy_model(self.model_id, "{}-copy".format(self.label))
        assert response.label == "{}-copy".format(self.label)

        # clean up
        self.api.delete_model(response.id)

    def testGetModels(self):
        """Test Get Models"""
        models = self.api.get_models().to_dict()["model_list"]
        assert self.model_id in [m["id"] for m in models]

    def testGetModel(self):
        """Test Get Model"""
        model = self.api.get_model(self.model_id)
        assert self.model_id == model.id
        assert self.label == model.label

    def testUpdateLabel(self):
        """Test Put Model"""
        model = self.api.update_label(self.model_id, "{}-update".format(self.label))
        assert self.model_id == model.id
        assert "{}-update".format(self.label) == model.label

    def testDeleteModel(self):
        """Test Delete Model"""

        #create separate model to test delete
        postModels = boonamber.PostModelRequest(label=self.label)
        model = self.api.post_model(postModels)
        assert model.label == self.label

        # get all old tests licenses
        models = self.api.get_models().to_dict()["model_list"]
        assert self.model_id in [m["id"] for m in models]
        models = [m for m in models if m["label"] == self.label and m["id"] != self.model_id]

        # test delete
        for m in models:
            self.api.delete_model(m["id"])

        models = self.api.get_models().to_dict()["model_list"]
        assert model.id not in [m["id"] for m in models]

    # TODO: JAT, get migrate tests working
    def testMigrate(self):
        """Test Migrate"""
        pass
        #sensor_id = self.v1.create_sensor(f"{self.label}-migrate")
        #v1_sensor = self.v1.get_sensor(sensor_id)
        #self.v1.configure_sensor(sensor_id, feature_count=1)

        #mid = self.api.migrate_model(sensor_id)

        #assert v1_sensor["label"] == mid.label

        #self.api.delete_model(mid.id)
        #self.v1.delete_sensor(v1_sensor["sensorId"])


if __name__ == '__main__':
    unittest.main()
