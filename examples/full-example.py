import sys
import boonamber as amber


"""Example usage of each Amber SDK endpoint."""


# set API credentials
amber.set_credentials(api_key='api-key', api_tenant='api-tenant')

# list all sensors in tenant namespace
success, response = amber.list_sensors()
if not success:
    print("could not list sensors: {}".format(response))
    sys.exit(1)
print("current sensors: {}".format(response))

# create a new sensor
success, response = amber.create_sensor('sample-sensor')
if not success:
    print("could not create sensor: {}".format(response))
    sys.exit(1)

# get usage info on a sensor
success, response = amber.get_info('sample-sensor')
if not success:
    print("could not get sensor info: {}".format(response))
    sys.exit(1)
print("sample-sensor usage info: {}".format(response))

# configure a sensor
success, response = amber.configure_sensor('sample-sensor', feature_count=1, streaming_window=25)
if not success:
    print("could not configure sensor: {}".format(response))
    sys.exit(1)

# get sensor configuration
success, response = amber.get_config('sample-sensor')
if not success:
    print("could not get configuration: {}".format(response))
    sys.exit(1)
print("sample-sensor config: {}".format(response))

# train a sensor on some historical data
data = [0.1, 0.2, 0.3, 0.4, 0.5]
success, response = amber.train_sensor('sample-sensor', data)
if not success:
    print("could not train sensor: {}".format(response))
    sys.exit(1)

# stream data to a sensor
data = [0.1, 0.2, 0.3, 0.4, 0.5]
success, response = amber.stream_sensor('sample-sensor', data)
if not success:
    print("could not stream data: {}".format(response))
    sys.exit(1)
print("streamed data: {} -> {}".format(data, results['SI']))

# get clustering status info from a sensor
success, response = amber.get_status('sample-sensor')
if not success:
    print("could not get sensor status: {}".format(response))
    sys.exit(1)
print("sample-sensor clustering status: {}".format(response))

# delete a sensor instance
success, response = amber.delete_sensor('sample-sensor')
if not success:
    print(response)
    sys.exit(1)
