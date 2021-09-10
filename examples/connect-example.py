import sys
import json
from boonamber import AmberClient, AmberCloudError, AmberUserError

# if you wish to turn off tls certificate warnings
# import urllib3
# urllib3.disable_warnings()
#
# Alternatively invoke python with -Wignore
#

# At initialization the client discovers Amber account credentials
# under the "default" entry in the ~/.Amber.license file.
#amber = AmberClient(verify=False)
amber = AmberClient()

try:
    # Get a list of all sensors belonging to the current user.
    version_info = amber.get_version()
except AmberCloudError as e:
    # AmberCloudError is raised upon any error response from the Amber server.
    print("Amber Cloud error: {}".format(e))
    sys.exit(1)
except AmberUserError as e:
    # AmberUserError is raised upon client-side usage errors with the SDK.
    print("Amber user error: {}".format(e))
    sys.exit(1)

print(json.dumps(version_info, indent=4))
