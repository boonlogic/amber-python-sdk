import csv
from boonamber import AmberClient

"""Demonstrates a streaming use case in which we read continuously
   from a CSV file, inference the data line by line, and print results.
"""

# initialize client
amber = AmberClient()

# look for a sensor labeled 'stream-example-sensor'; if not there, create it
sensors = amber.list_sensors()
for sensor_id, label in sensors.items():
    if label == 'stream-example-sensor':
        break
else:
    sensor_id = amber.create_sensor(label='stream-example-sensor')
    print("created sensor {}".format(sensor_id))

print("using sensor {}".format(sensor_id))

# configure the sensor: feature_count is 3 since our CSV data has three columns
config = amber.configure_sensor(sensor_id, feature_count=3, streaming_window_size=25)
print("config: {}".format(config))

# open data file and begin streaming!
with open('data.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')

    for row in reader:
        data = [float(d) for d in row]

        result = amber.stream_sensor(sensor_id, data)
        state = result['state']
        anomaly_index = result['SI'][0]

        data_pretty = ' '.join("{:5.2f}".format(d) for d in data)
        print("{} [{}] -> {}".format(state, data_pretty, anomaly_index))
