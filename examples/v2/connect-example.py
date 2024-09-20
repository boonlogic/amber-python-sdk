import sys
import json
from boonamber import AmberV2Client, ApiException

# At initialization the client discovers Amber account credentials
# under the "default" profile entry in the ~/.Amber.license file.
try:
    # Use default ~/.Amber.license file
    amber = AmberV2Client(profile_name="python-sdk-v2")
    version_info = amber.get_version()
except ApiException as e:
    print(f"Error: {e}")
    sys.exit(1)

print(json.dumps(version_info.to_dict(), indent=4))
