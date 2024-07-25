import csv
import sys
import json
import time
from boonamber import AmberV2Client, ApiException
import boonamber

"""Demonstrates pretraining of data in a CSV file."""

model_id = None  # fill this in if a model has already been created.

def cleanup():
    if model_id is not None:
        print("cleanup: deleting model {}".format(model_id))
        amber.delete_model(model_id)

# load csv_file
data = []
with open('output_current.csv', 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    for row in csv_reader:
        data.extend(row)

try:
    amber = AmberV2Client()

    # Create a new model
    if model_id is None:
        print("creating model")
        param = boonamber.PostModelRequest(label='amber.sdk.example')
        model = amber.post_model(param)
        print(json.dumps(model.to_dict(), indent=4))
        model_id = model.id
        print()

    # Configure the model
    print("configuring model")
    body = boonamber.PostConfigRequest(streaming_window=25, features=[boonamber.FeatureConfig("feature-1")])
    config_result = amber.post_config(model_id=model_id, body=body)

    print("running pretraining, block until complete")
    results = amber.post_pretrain(model_id=model_id, data=data, block=True)
    print(json.dumps(results.to_dict(), indent=4))

    print("get status of pretrained model")
    status = amber.get_status(model_id)
    print(status)

    cleanup()
    print("succeeded")

except ApiException as e:
    print(e)
    cleanup()
    sys.exit(1)
