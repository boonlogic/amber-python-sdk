import sys
import boonamber as amber


"""A basic proof-of-connectivity with the Amber server."""


# set API credentials
amber.set_credentials(api_key='api-key', api_tenant='api-tenant')

# list current sensors in tenant namespace
success, response = amber.sensor_list()
if not success:
    print("could not list sensors: {}".format(response))
    sys.exit(1)
print("sensors: {}".format(response))
