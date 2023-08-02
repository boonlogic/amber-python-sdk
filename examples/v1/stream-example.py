import csv
import sys
from boonamber import AmberClient, AmberCloudError

"""Demonstrates a streaming use case in which we read continuously
   from a CSV file, inference the data line by line, and print results.
"""

amber = AmberClient()

sensor_id = 'put-created-sensor-id-here'

# The commented out block below creates a new sensor and prints the
# corresponding sensor ID. These lines should be uncommented the first
# time this script is run to create the sensor which is used for this
# example. For any following runs, these lines should be commented out
# again and the created sensor ID should be filled into the line above
# so that the same sensor is accessed on subsequent runs.

try:
    sensor_id = amber.create_sensor(label='python.sdk.example:stream')
except AmberCloudError as e:
    print(e)
    sys.exit(1)
print("created sensor {}".format(sensor_id))

# print("using sensor {}".format(sensor_id))

# Configure the sensor: feature_count is 3 since our CSV data has three columns
try:
    config = amber.configure_sensor(sensor_id, feature_count=3, streaming_window_size=25)
except AmberCloudError as e:
    print(e)
    sys.exit(1)
print("config: {}".format(config))

# Open data file and begin streaming!
with open('data.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')

    for row in reader:
        data = [float(d) for d in row]

        try:
            result = amber.stream_sensor(sensor_id, data)
        except AmberCloudError as e:
            print(e)
            sys.exit(1)

        state = result['state']
        anomaly_index = result['SI'][0]

        data_pretty = ' '.join("{:5.2f}".format(d) for d in data)
        print("{} [{}] -> {}".format(state, data_pretty, anomaly_index))
