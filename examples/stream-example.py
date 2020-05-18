import csv
import sys
import boonamber as amber


"""Demonstrates a streaming use case in which we read continuously
   from a CSV file, inference the data line by line, and write results
   out to another file.
"""


IN_FILE = 'data.csv'
OUT_FILE = 'results.csv'
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

# open CSV files and begin streaming!
with open(OUT_FILE, 'w') as f_out:
    with open(IN_FILE, 'r') as f_in:
        reader = csv.reader(f_in, delimiter=',')

        for data_row in reader:
            success, result = amber.stream_sensor(SENSOR_ID, data_row)
            if not success:
                print("could not stream data: {}".format(result))
                sys.exit(1)

            print("data: {}, anomaly index: {}".format(data_row, result))
            f_out.write('{}\n'.format(result))
