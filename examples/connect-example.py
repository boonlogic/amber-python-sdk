import sys
from boonamber import AmberClient, AmberCloudError, AmberUserError

# At initialization the client discovers Amber account credentials
# under the "default" entry in the ~/.Amber.license file.
amber = AmberClient()

try:
    # Get a list of all sensors belonging to the current user.
    sensors = amber.list_sensors()
except AmberCloudError as e:
    # AmberCloudError is raised upon any error response from the Amber server.
    print("Amber Cloud error: {}".format(e))
    sys.exit(1)
except AmberUserError as e:
    # AmberUserError is raised upon client-side usage errors with the SDK.
    print("Amber user error: {}".format(e))
    sys.exit(1)

print("sensors: {}".format(sensors))
