import csv
import sys
import json
from datetime import datetime
from boonamber import AmberV2Client, ApiException, float_list_to_csv_string
import boonamber

"""Demonstrates a streaming use case in which we read continuously
   from a CSV file, inference the data line by line, and print results.
"""

model_id = None  # fill this in if a model has already been created.

# load csv_file
data = []
with open('output_current.csv', 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    for row in csv_reader:
        data.extend(row)

try:
    amber = AmberV2Client()

    # Create a new model
    print("creating model")
    if model_id is None:
        param = boonamber.PostModelRequest(label='amber.sdk.example')
        model = amber.post_model(param)
        print(json.dumps(model.to_dict(), indent=4))
        model_id = model.id
        print()

    # Configure model
    print("configuring model")
    body = boonamber.PostConfigRequest(streaming_window=25, features=[boonamber.FeatureConfig("feature-1")],)
    config_result = amber.post_config(model_id=model_id, body=body)

    batch_size = 50
    while len(data) > 0:
        next_batch = data[:batch_size]
        data = data[batch_size:]
        results = amber.post_data(model_id, data=next_batch)
        status = results.status
        print(f"State: {status.state}({status.progress}%), inferences: {status.sample_count}, clusters: {status.cluster_count}, samples: {batch_size}")

except ApiException as e:
    print(f"Error: {e}")
    sys.exit(1)

