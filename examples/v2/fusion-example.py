import json
import sys

import boonamber
from boonamber import AmberV2Client, ApiException

"""Demonstrates usage of submitting data via the label for individual features of a fusion vector."""

try:
    amber = AmberV2Client()

    # Create a new model
    print("creating model")
    param = boonamber.PostModelRequest(label='amber.sdk.example')
    model = amber.post_model(param)
    print(json.dumps(model.to_dict(), indent=4))
    model_id = model.id
    print()

    # Configure a sensor
    print("configuring model")
    feature1 = boonamber.FeatureConfig(name="vibration.freq.1000hz", fusion_rule="submit")
    feature2 = boonamber.FeatureConfig(name="vibration.freq.2000hz", fusion_rule="submit")
    feature3 = boonamber.FeatureConfig(name="speed.sensor.1", fusion_rule="submit")
    feature4 = boonamber.FeatureConfig(name="feature-3", fusion_rule="submit")
    feature5 = boonamber.FeatureConfig(name="feature-4", fusion_rule="submit")
    param = boonamber.PostConfigRequest(streaming_window=25,
                                        features=[feature1, feature2, feature3, feature4, feature5]
                                        )
    config = amber.post_config(model_id, param)
    print(config.to_dict())
    print()

    #
    # Note: initially, the model will not be run until data has been set
    # for each feature. Once that has happened, each feature update runs the model
    # according to our submitRule values.
    #

    # the 3rd feature updated before any other feature, normal for fusion
    v2 = boonamber.FusionFeature(name=feature2.name, value=5)
    print("update: vector: {}".format(v2.to_dict()))
    body = boonamber.PutDataRequest(vector=[v2])
    resp = amber.put_data(model_id, body=body)

    # we always get the current vector back,
    # in this case, 'results' doesn't exist due to an incomplete vector
    print("resp: {}".format(resp))

    # update the rest of the features...
    v1 = boonamber.FusionFeature(name=feature1.name, value=16)
    v3 = boonamber.FusionFeature(name=feature3.name, value=34)
    v4 = boonamber.FusionFeature(name=feature4.name, value=84.5)
    v5 = boonamber.FusionFeature(name=feature5.name, value=0)

    body = boonamber.PutDataRequest(vector=[v1, v3, v4, v5])
    resp = amber.put_data(model_id, body=body)
    # we always get the current vector back, in this case, results are included
    print("resp.status: {}".format(resp.status))
    print("resp.vector: {}".format(resp.vector))
    print()

    # 5th feature updated:
    v5 = boonamber.FusionFeature(name=feature5.name, value=111.2)
    print("update: vector: {}".format(v5.to_dict()))
    body = boonamber.PutDataRequest(vector=[v5])
    resp = amber.put_data(model_id, body=body)
    # we always get the current vector back, in this case, results are included
    print("resp.status: {}".format(resp.status))
    print("resp.vector: {}".format(resp.vector))
    print()

    # Delete the model instance
    print("cleanup: deleting model {}".format(model_id))
    result = amber.delete_model(model_id)
    print("succeeded")

except ApiException as e:
    print(f"Error: {e}")
    sys.exit(1)
