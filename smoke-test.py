from boonamber import AmberClient


amber = AmberClient()

# authenticate
print("authenticating")
success, response = amber.authenticate('amber-test-user', r'UFGdMzt*P1Zv*4%b')
print("success: {}, response: {}".format(success, response))
print()

# list sensors
print("listing sensors")
success, response = amber.list_sensors()
print("success: {}, response: {}".format(success, response))
print()

# create sensor
print("creating sensor")
success, sensor_id = amber.create_sensor('test-sensor')
print("success: {}, response: {}".format(success, sensor_id))
print()

# getting sensor
print("getting sensor")
success, response = amber.get_sensor(sensor_id)
print("success: {}, response: {}".format(success, response))
print()

# configure sensor
print("configuring sensor")
success, response = amber.configure_sensor(sensor_id, features=1, streaming_window_size=25)
print("success: {}, response: {}".format(success, response))
print()

# get configuration
print("getting configuration")
success, response = amber.get_config(sensor_id)
print("success: {}, response: {}".format(success, response))
print()

# stream data
print("streaming data")
success, response = amber.stream_sensor(sensor_id, [0, 1, 2, 3, 4])
print("success: {}, response: {}".format(success, response))
print()

# get status
print("getting status")
success, response = amber.get_status(sensor_id)
print("success: {}, response: {}".format(success, response))
print()

# delete sensor
print("deleting sensor")
success, response = amber.delete_sensor(sensor_id)
print("success: {}, response: {}".format(success, response))
print()
