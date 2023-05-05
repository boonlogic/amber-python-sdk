import sys
import json
from boonamber import AmberV2Client, v2models, ApiException

"""Demonstrates usage of all Amber SDK endpoints."""

# connect with default license
# use 'license_id=<name>' to specify something other than 'default'
amber = AmberV2Client()

# List all sensors belonging to current user
print("getting version info")
try:
    version_info = amber.get_version()
    print(json.dumps(version_info.to_dict(), indent=4))
    print()
except ApiException as e:
    print(e)
    sys.exit(1)

# List all models belonging to current user
print("listing models")
try:
    models = amber.get_models()
    print(json.dumps(models.to_dict(), indent=4))
    print()
except ApiException as e:
    print(e)
    sys.exit(1)

# Create a new model
print("creating model")
try:
    param = v2models.PostModelRequest(label='amber.sdk.example.v2:full')
    model = amber.post_model(param)
    print(json.dumps(model.to_dict(), indent=4))
    model_id = model.id
    print()
except ApiException as e:
    print(e)
    sys.exit(1)

# Get sensor info
print("getting model")
try:
    model = amber.get_model(model_id)
    print(json.dumps(model.to_dict(), indent=4))
    print()
except ApiException as e:
    print(e)
    sys.exit(1)

# Update the label of a sensor
print("updating label")
try:
    param = v2models.PutModelRequest(label='amber.sdk.example.v2:full-updated')
    label = amber.put_model(model_id, param)
    print(json.dumps(label.to_dict(), indent=4))
    print()
except ApiException as e:
    print(e)
    sys.exit(1)

# Configure a sensor
print("configuring model")
try:
    feature1 = v2models.FeatureConfig("feature-1")
    feature2 = v2models.FeatureConfig("feature-2")
    feature3 = v2models.FeatureConfig("feature-3")
    param = v2models.PostConfigRequest(streaming_window=25, features=[feature1,feature2,feature3])
    config = amber.post_model_config(model_id, param)
    print(json.dumps(config.to_dict(), indent=4))
    print()
except ApiException as e:
    print(e)
    sys.exit(1)

# Get sensor configuration
print("getting configuration")
try:
    config = amber.get_model_config(model_id)
    print(json.dumps(config.to_dict(), indent=4))
    print()
except ApiException as e:
    print(e)
    sys.exit(1)

# Stream data to a sensor
print("streaming data")
param = v2models.PostDataRequest(data="0,1,2", save_image=False)
try:
    results = amber.post_model_data(model_id, param)
    print(json.dumps(results.to_dict(), indent=4))
    print()
except ApiException as e:
    print(e)
    sys.exit(1)

# Get clustering status from a sensor
print("getting status")
try:
    status = amber.get_model_status(model_id)
    print(json.dumps(status.to_dict(), indent=4))
    print()
except ApiException as e:
    print(e)
    sys.exit(1)

# Post Outage
print("post outage")
try:
    post_outage = amber.post_model_outage(model_id)
    print(json.dumps(post_outage.to_dict(), indent=4))
    print()
except ApiException as e:
    print(e)
    sys.exit(1)

# Get clustering status from a model
#print("getting root cause")
#try:
#    root_cause = amber.get_model_root_cause(model_id, clusters="[1, 2]")
#except ApiException as e:
#    print(e)
#    sys.exit(1)
#print("root cause: {}".format(root_cause))
#print()

# Enable learning
print("enabling learning")
try:
    #training_config = v2models.TrainingConfig(history_window=10000, buffering_samples=10000,
    #                                          learning_max_samples=10000, learning_max_clusters=1000,
    #                                          learning_rate_numerator=10, learning_rate_denominator=10000)
    training_config = v2models.TrainingConfig()
    params = v2models.PostLearningRequest(training=None)
    enable_learning = amber.post_model_enable_learning(model_id=model_id, body=params)
    print(json.dumps(enable_learning.to_dict(), indent=4))
    print()
except ApiException as e:
    print(e.status, e.body)
    #    print(e)
    #    sys.exit(1)
    #else:
    #    print(e.body)
print()

# Get Nano Status
# Get clustering status from a sensor
print("getting nano status")
try:
    status = amber.get_model_nano_status(model_id)
    print(json.dumps(status.to_dict(), indent=4))
    print()
except ApiException as e:
    print(e)
    sys.exit(1)

# Delete a model instance
print("deleting model")
try:
    result = amber.delete_model(model_id)
    print(json.dumps(result.to_dict(), indent=4))
    print()
except ApiException as e:
    print(e)
    sys.exit(1)
