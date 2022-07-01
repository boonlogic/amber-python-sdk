import sys
import json
from boonamber import AmberClient, AmberCloudError, AmberUserError

"""Demonstrates usage of submitting data via the label for individual features of a fusion vector."""

def dump_resp_vector(resp):
    resp_vector = resp['vector'].split(",")
    print("resp.vector: {}".format(resp['vector']))
    for i in range(len(features)):
        print("resp.vector[{}] => {}\t<= {}".format(i, resp_vector[i], features[i]['label']))
    print()

def cleanup():
    if 'sensor_id' in globals():
        # Clean up
        print("cleanup: deleting sensor {}".format(sensor_id))
        amber.delete_sensor(sensor_id)
        print("succeeded.")
    print()

# connect with default license
amber = AmberClient(license_id='default')

try:
    # List all sensors belonging to current user
    print("getting version info")
    version_info = amber.get_version()
    print(json.dumps(version_info, indent=4))

    # Create a new sensor
    print("creating sensor")
    sensor_id = amber.create_sensor('fusion-example-sensor')
    print("sensor-id: {}".format(sensor_id))
    print()

    # This will be a 5 feature fusion vector. As each feature
    # gets updated it will run the model (submitRule = 'submit').
    # If a feature gets updated frequently, we may not want to run the model,
    # in that case set submitRule = 'nosubmit'.
    #
    # Keep in mind, the labels:
    # - must be unique within the model
    # - the label field is to be used when submitting new data
    # - the feature order in the results vector is the same as the configured features order
    #
    features = []
    features.append({ "label": "vibration.freq.1000hz", "submitRule": "submit"})
    features.append({ "label": "vibration.freq.2000hz", "submitRule": "submit"})
    features.append({ "label": "speed-sensor-1", "submitRule": "submit"})
    features.append({ "label": "f3", "submitRule": "submit"})
    features.append({ "label": "f4", "submitRule": "submit"})

    # Configure a sensor
    #
    # Here is where you could set different model parameters:
    exsamples = 100000

    print("configuring sensor")
    config = amber.configure_sensor(sensor_id, feature_count=len(features), streaming_window_size=1, learning_max_samples=exsamples, features=features)
    print("config: {}".format(config))
    print()

    #
    # Keep in mind, initially the model will not be run until data has been set
    # for each feature. Once that has happened, each feature update runs the model
    # according to our submitRule values.
    #

    # Hey look, the 3rd feature updated before any other feature:
    v = [{'label': features[2]['label'], 'value': 5}]
    print("update: vector: {}".format(v))
    resp = amber.stream_fusion(sensor_id, vector=v)

    # we always get the current vector back,
    # in this case, 'results' doesn't exist due to an incomplete vector
    print("resp: {}".format(resp))
    dump_resp_vector(resp)

    # update the rest of the features...
    v = []
    v.append({'label':features[0]['label'], 'value': 16})
    v.append({'label':features[1]['label'], 'value': 34})
    v.append({'label':features[3]['label'], 'value': 84.5})
    v.append({'label':features[4]['label'], 'value': 0})

    print("update: vector: {}".format(v))
    resp = amber.stream_fusion(sensor_id, vector=v)
    # we always get the current vector back, in this case, results are included
    print("resp: {}".format(resp))
    print("resp.results: {}".format(resp['results']))
    dump_resp_vector(resp)

    # 5th feature updated:
    v = [{'label': features[4]['label'], 'value': 111.2}]
    print("update: vector: {}".format(v))
    resp = amber.stream_fusion(sensor_id, vector=v)
    # we always get the current vector back, in this case, results are included
    print("resp: {}".format(resp))
    print("resp.results: {}".format(resp['results']))
    dump_resp_vector(resp)

except Exception as e:
    print("{} error: {}".format(type(e).__name__, e))
    cleanup()
    sys.exit(1)

try:
    cleanup()
except Exception as e:
    print("{} error: {}".format(type(e).__name__, e))
    sys.exit(1)

