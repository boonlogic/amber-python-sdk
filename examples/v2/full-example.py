import sys
import json
from boonamber import AmberV2Client, ApiException
import boonamber

"""Demonstrates usage of all Amber SDK endpoints."""

# connect with default license
# use 'license_id=<name>' to specify something other than 'default'
amber = AmberV2Client.from_license_file()

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
    param = boonamber.PostModelRequest(label='amber.sdk.example.v2:full')
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
    label = amber.update_label(model_id, 'amber.sdk.example.v2:full-updated')
    print(json.dumps(label.to_dict(), indent=4))
    print()
except ApiException as e:
    print(e)
    sys.exit(1)

# Configure a sensor
print("configuring model")
try:
    feature1 = boonamber.FeatureConfig("feature-1")
    feature2 = boonamber.FeatureConfig("feature-2")
    feature3 = boonamber.FeatureConfig("feature-3")
    param = boonamber.PostConfigRequest(streaming_window=25, features=[feature1,feature2,feature3])
    config = amber.post_config(model_id, param)
    print(json.dumps(config.to_dict(), indent=4))
    print()
except ApiException as e:
    print(e)
    sys.exit(1)

# Get sensor configuration
print("getting configuration")
try:
    config = amber.get_config(model_id)
    print(json.dumps(config.to_dict(), indent=4))
    print()
except ApiException as e:
    print(e)
    sys.exit(1)

# Stream data to a sensor
print("streaming data")
try:
    results = amber.post_data(model_id, data="0,1,2", save_image=False)
    print(json.dumps(results.to_dict(), indent=4))
    print()
except ApiException as e:
    print(e)
    sys.exit(1)

# Get clustering status from a sensor
print("getting status")
try:
    status = amber.get_status(model_id)
    print(json.dumps(status.to_dict(), indent=4))
    print()
except ApiException as e:
    print(e)
    sys.exit(1)

# Post Outage
print("post outage")
try:
    amber.post_outage(model_id)
    print("success")
    print()
except ApiException as e:
    print(e)
    sys.exit(1)

# Get clustering status from a model
#print("getting root cause")
#try:
#    root_cause = amber.get_root_cause(model_id, clusters="[1, 2]")
#except ApiException as e:
#    print(e)
#    sys.exit(1)
#print("root cause: {}".format(root_cause))
#print()

# Enable learning
print("enabling learning")
try:
    #training_config = boonamber.TrainingConfig(history_window=10000, buffering_samples=10000,
    #                                          learning_max_samples=10000, learning_max_clusters=1000,
    #                                          learning_rate_numerator=10, learning_rate_denominator=10000)
    training_config = boonamber.TrainingConfig()
    enable_learning = amber.enable_learning(model_id=model_id, training=training_config)
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
    status = amber.get_nano_status(model_id)
    print(json.dumps(status.to_dict(), indent=4))
    print()
except ApiException as e:
    print(e)
    sys.exit(1)

# Delete a model instance
print("deleting model")
try:
    amber.delete_model(model_id)
    print('success')
    print()
except ApiException as e:
    print(e)
    sys.exit(1)
