import sys
from boonamber import AmberClient, AmberCloudError, AmberUserError

"""Demonstrates usage of all Amber SDK endpoints."""

# connect with default license
# use 'license_id=<name>' to specify something other than 'default'
amber = AmberClient(verify=False)

# List all sensors belonging to current user
print("listing sensors")
try:
    sensors = amber.list_sensors()
except AmberCloudError as e:
    print(e)
    sys.exit(1)
except AmberUserError as e:
    print(e)
    sys.exit(1)
print("sensors: {}".format(sensors))
print()

# Create a new sensor
print("creating sensor")
try:
    sensor_id = amber.create_sensor('new-test-sensor')
except AmberCloudError as e:
    print(e)
    sys.exit(1)
except AmberUserError as e:
    print(e)
    sys.exit(1)
print("sensor-id: {}".format(sensor_id))
print()

# Get sensor info
print("getting sensor")
try:
    sensor = amber.get_sensor(sensor_id)
except AmberCloudError as e:
    print("Amber Cloud error: {}".format(e))
    sys.exit(1)
except AmberUserError as e:
    print("Amber user error: {}".format(e))
    sys.exit(1)
print("sensor: {}".format(sensor))
print()

# Update the label of a sensor
print("updating label")
try:
    label = amber.update_label(sensor_id, 'test-sensor')
except AmberCloudError as e:
    print("Amber Cloud error: {}".format(e))
    sys.exit(1)
except AmberUserError as e:
    print("Amber user error: {}".format(e))
    sys.exit(1)
print("label: {}".format(label))
print()

# Configure a sensor
print("configuring sensor")
try:
    config = amber.configure_sensor(sensor_id, feature_count=1, streaming_window_size=25)
except AmberCloudError as e:
    print("Amber Cloud error: {}".format(e))
    sys.exit(1)
except AmberUserError as e:
    print("Amber user error: {}".format(e))
    sys.exit(1)
print("config: {}".format(config))
print()

# Get sensor configuration
print("getting configuration")
try:
    config = amber.get_config(sensor_id)
except AmberCloudError as e:
    print("Amber Cloud error: {}".format(e))
    sys.exit(1)
except AmberUserError as e:
    print("Amber user error: {}".format(e))
    sys.exit(1)
print("config: {}".format(config))
print()

# Stream data to a sensor
print("streaming data")
data = [0, 1, 2, 3, 4]
try:
    results = amber.stream_sensor(sensor_id, data)
except AmberCloudError as e:
    print("Amber Cloud error: {}".format(e))
    sys.exit(1)
except AmberUserError as e:
    print("Amber user error: {}".format(e))
    sys.exit(1)
print("results: {},".format(results))
print()

# Get clustering status from a sensor
print("getting status")
try:
    status = amber.get_status(sensor_id)
except AmberCloudError as e:
    print("Amber Cloud error: {}".format(e))
    sys.exit(1)
except AmberUserError as e:
    print("Amber user error: {}".format(e))
    sys.exit(1)
print("status: {}".format(status))
print()

# Delete a sensor instance
#print("deleting sensor")
#try:
#    amber.delete_sensor(sensor_id)
#except AmberCloudError as e:
#    print("Amber Cloud error: {}".format(e))
#    sys.exit(1)
#except AmberUserError as e:
#    print("Amber user error: {}".format(e))
#    sys.exit(1)
print("succeeded")
print()
