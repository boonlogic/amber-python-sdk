import sys
import json
from boonamber import AmberV2Client, ApiException

try:
    # Use ~/.Amber.license file and "default" profile
    amber = AmberV2Client()
    version_info = amber.get_version()
except ApiException as e:
    print(f"Error: {e}")
    sys.exit(1)

print(json.dumps(version_info.to_dict(), indent=4))
