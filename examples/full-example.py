from boonamber import AmberClient

"""Demonstrates usage of all Amber SDK endpoints."""

amber = AmberClient()

# authenticate client
print("authenticating")
amber.authenticate()
print("succeeded")
print()

# list all sensors belonging to current user
print("listing sensors")
sensors = amber.list_sensors()
print("sensors: {}".format(sensors))
print()

# create a new sensor
print("creating sensor")
sensor_id = amber.create_sensor('new-test-sensor')
print("sensor-id: {}".format(sensor_id))
print()

# get sensor info
print("getting sensor")
sensor = amber.get_sensor(sensor_id)
print("sensor: {}".format(sensor))
print()

# update the label of a sensor
print("updating label")
label = amber.update_label(sensor_id, 'test-sensor')
print("sensor: {}".format(label))
print()

# configure a sensor
print("configuring sensor")
config = amber.configure_sensor(sensor_id, features=1, streaming_window_size=25)
print("config: {}".format(config))
print()

# get sensor configuration
print("getting configuration")
config = amber.get_config(sensor_id)
print("config: {}".format(config))
print()

# stream data to a sensor
print("streaming data")
data = [0, 1, 2, 3, 4]
results = amber.stream_sensor(sensor_id, data)
print("results: {},".format(results))
print()

# get clustering status from a sensor
print("getting status")
status = amber.get_status(sensor_id)
print("status: {}".format(status))
print()

# delete a sensor instance
print("deleting sensor")
amber.delete_sensor(sensor_id)
print("succeeded")
print()
