import boonamber as amber
import sys

# set API credentials
amber.set_credentials(api_key='api-key', api_tenant='api-tenant')

# list current sensors in tenant namespace
success, response = amber.list_sensors()
if not success:
    print("could not list sensors: {}".format(response))
    sys.exit(1)
print("sensors: {}".format(response))
