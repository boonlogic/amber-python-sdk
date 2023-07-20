import sys
import json
from boonamber import AmberV2Client, ApiException

# if you wish to turn off tls certificate warnings
# import urllib3
# urllib3.disable_warnings()
#
# Alternatively invoke python with -Wignore
#

# At initialization the client discovers Amber account credentials
# under the "default" entry in the ~/.Amber.license file.
#amber = AmberClient(verify=False)
amber = AmberV2Client.from_license_file()

try:
    # Get a list of all sensors belonging to the current user.
    version_info = amber.get_version()
except ApiException as e:
    print("Amber Cloud error: {}".format(e))
    sys.exit(1)

print(json.dumps(version_info.to_dict(), indent=4))
