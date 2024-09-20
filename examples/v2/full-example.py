import sys
import json
from boonamber import AmberV2Client, ApiException
import boonamber

"""Demonstrates usage of core Amber SDK endpoints."""

try:
    amber = AmberV2Client()

    # version information
    print("get version info:")
    version_info = amber.get_version()
    print(json.dumps(version_info.to_dict(), indent=4))
    print()

    # List all models belonging to current user
    print("get list of models")
    models = amber.get_models()
    print(json.dumps(models.to_dict(), indent=4))
    print()

    # Create a new model
    print("create a new model:")
    param = boonamber.PostModelRequest(label='amber.sdk.example.v2:full')
    model = amber.post_model(param)
    print(json.dumps(model.to_dict(), indent=4))
    model_id = model.id
    print()

    # Get model info
    print("get model info:")
    model = amber.get_model(model_id)
    print(json.dumps(model.to_dict(), indent=4))
    print()

    # Update label for model
    print("update model label:")
    label = amber.update_label(model_id, 'amber.sdk.example.v2:full-updated')
    print(json.dumps(label.to_dict(), indent=4))
    print()

    # configure the model
    print("configure the model:")
    feature1 = boonamber.FeatureConfig("feature-1")
    feature2 = boonamber.FeatureConfig("feature-2")
    feature3 = boonamber.FeatureConfig("feature-3")
    param = boonamber.PostConfigRequest(streaming_window=25, features=[feature1,feature2,feature3])
    config = amber.post_config(model_id, param)
    print(json.dumps(config.to_dict(), indent=4))
    print()

    # Get model configuration
    print("get model configuration")
    config = amber.get_config(model_id)
    print(json.dumps(config.to_dict(), indent=4))
    print()

    # Stream data to model
    print("post data to the model:")
    results = amber.post_data(model_id, data="0,1,2", save_image=False)
    print(json.dumps(results.to_dict(), indent=4))
    print()

    # Get clustering status for model
    print("get status for model:")
    status = amber.get_status(model_id)
    print(json.dumps(status.to_dict(), indent=4))
    print()

    # Get Nano status for model
    print("get_nano_status:")
    status = amber.get_nano_status(model_id)
    print(json.dumps(status.to_dict(), indent=4))
    print()

    # Delete a model instance
    print("deleting model")
    amber.delete_model(model_id)
    print('success')
    print()

except ApiException as e:
    print(f"Error: {e}")
    sys.exit(1)
