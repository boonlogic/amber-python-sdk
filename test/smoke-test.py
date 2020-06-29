from boonamber import AmberClient


amber = AmberClient()

# authenticate
print("authenticating")
amber.authenticate('amber-test-user', r'UFGdMzt*P1Zv*4%b')
print("succeeded")
print()

# list sensors
print("listing sensors")
sensors = amber.list_sensors()
print("sensors: {}".format(sensors))
print()

# create sensor
print("creating sensor")
sensor_id = amber.create_sensor('test-sensor')
print("sensor-id: {}".format(sensor_id))
print()

# getting sensor
print("getting sensor")
sensor = amber.get_sensor(sensor_id)
print("sensor: {}".format(sensor))
print()

# configure sensor
print("configuring sensor")
config = amber.configure_sensor(sensor_id, features=1, streaming_window_size=25)
print("config: {}".format(config))
print()

# get configuration
print("getting configuration")
config = amber.get_config(sensor_id)
print("config: {}".format(config))
print()

# stream data
print("streaming data")
results = amber.stream_sensor(sensor_id, [0, 1, 2, 3, 4])
print("results: {},".format(results))
print()

# get status
print("getting status")
status = amber.get_status(sensor_id)
print("status: {}".format(status))
print()

# delete sensor
print("deleting sensor")
amber.delete_sensor(sensor_id)
print("succeeded")
print()
