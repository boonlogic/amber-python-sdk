import sys
import json
from boonamber import AmberV2Client, v2models, ApiException

"""Demonstrates usage of submitting data via the label for individual features of a fusion vector."""

# connect with default license
# use 'license_id=<name>' to specify something other than 'default'
amber = AmberV2Client()

# Create a new model
print("creating model")
try:
    param = v2models.PostModelRequest(label='amber.sdk.example.v2:fusion')
    model = amber.post_model(param)
    print(json.dumps(model.to_dict(), indent=4))
    model_id = model.id
    print()
except ApiException as e:
    print(e)
    sys.exit(1)

# Configure a sensor
print("configuring model")
try:
    feature1 = v2models.FeatureConfig(id="vibration.freq.1000hz", fusion_rule="submit")
    feature2 = v2models.FeatureConfig(id="vibration.freq.2000hz", fusion_rule="submit")
    feature3 = v2models.FeatureConfig(id="speed.sensor.1", fusion_rule="submit")
    feature4 = v2models.FeatureConfig(id="feature-3", fusion_rule="submit")
    feature5 = v2models.FeatureConfig(id="feature-4", fusion_rule="submit")
    param = v2models.PostConfigRequest(streaming_window=25,
                                       features=[feature1,feature2,feature3,feature4,feature5]
                                      )
    config = amber.post_model_config(model_id, param)
    print(config.to_dict())
    print()
except ApiException as e:
    print(e)
    sys.exit(1)

#
# Keep in mind, initially the model will not be run until data has been set
# for each feature. Once that has happened, each feature update runs the model
# according to our submitRule values.
#

# Hey look, the 3rd feature updated before any other feature:
v2 = v2models.FusionFeature(name=feature2.id, value=5)
print("update: vector: {}".format(v2.to_dict()))
body = v2models.PutDataRequest(vector=[v2])
resp = amber.put_model_data(model_id, body=body)

# we always get the current vector back,
# in this case, 'results' doesn't exist due to an incomplete vector
print("resp: {}".format(resp))


# update the rest of the features...
v1 = v2models.FusionFeature(name=feature1.id, value=16)
v3 = v2models.FusionFeature(name=feature3.id, value=34)
v4 = v2models.FusionFeature(name=feature4.id, value=84.5)
v5 = v2models.FusionFeature(name=feature5.id, value=0)

body = v2models.PutDataRequest(vector=[v1,v3, v4, v5])
resp = amber.put_model_data(model_id, body=body)
# we always get the current vector back, in this case, results are included
print("resp.status: {}".format(resp.status))
print("resp.vector: {}".format(resp.vector))
print()

# 5th feature updated:
v5 = v2models.FusionFeature(name=feature5.id, value=111.2)
print("update: vector: {}".format(v5.to_dict()))
body = v2models.PutDataRequest(vector=[v5])
resp = amber.put_model_data(model_id, body=body)
# we always get the current vector back, in this case, results are included
print("resp.status: {}".format(resp.status))
print("resp.vector: {}".format(resp.vector))
print()

# Delete the model instance
print("cleanup: deleting model {}".format(model_id))
try:
    result = amber.delete_model(model_id)
    print("succeeded")
except ApiException as e:
    print(e)
    sys.exit(1)
