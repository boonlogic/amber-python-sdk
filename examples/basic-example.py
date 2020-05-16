import sys
import boonamber as amber


"""Demonstrates basic sensor creation and streaming."""


# set API credentials
amber.set_credentials(api_key='api-key', api_tenant='api-tenant')

# create a new sensor
success, response = amber.create_sensor('sample-sensor')
if not success:
    print("could not create sensor: {}".format(response))
    sys.exit(1)

# stream data to the sensor and print the resulting analytics
success, response = amber.stream_sensor('sample-sensor', [0, 1, 2, 3, 4])
if not success:
    print("could not stream data: {}".format(response))
    sys.exit(1)
print(response['SI'])

# delete the sensor
success, response = amber.delete_sensor('sample-sensor')
if not success:
    print("could not delete sensor: {}".format(response))
    print(response)
    sys.exit(1)
