import csv
import sys
import boonamber as amber


"""Demonstrates training a sensor on a CSV file of historical data."""


DATA_FILE = 'data.csv'
SENSOR_ID = 'stream-example-sensor'


# set API credentials
amber.set_credentials(api_key='api-key', api_tenant='api-tenant')

# create sensor if needed
success, current_sensors = amber.list_sensors()
if not success:
    print("could not list sensors: {}".format(current_sensors))
    sys.exit(1)

if SENSOR_ID not in current_sensors:
    success, response = amber.create_sensor(SENSOR_ID)

# configure the sensor -- feature_count is 3 since our CSV data has three columns
success, response = amber.configure_sensor(SENSOR_ID, feature_count=3, streaming_window=10)
if not success:
    print("could not configure sensor: {}".format(response))
    sys.exit(1)

# read CSV data into a list-of-lists
with open(DATA_FILE, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    data = [[float(d) for d in row] for row in reader]

# train sensor on this data
success, response = amber.train_sensor(SENSOR_ID, data)
if not success:
    print("could not configure sensor: {}".format(response))
    sys.exit(1)

print("training succeeded")
