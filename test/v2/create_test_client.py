import os
from ..amber_secrets import get_secrets
from boonamber import (AmberV2Client)

def create_test_client():
    amber_license_file = os.environ.get('AMBER_TEST_LICENSE_FILE', None)
    amber_license_id = os.environ.get('AMBER_TEST_LICENSE_ID', None)
    assert amber_license_id is not None, 'AMBER_TEST_LICENSE_ID is missing in test environment'

    if amber_license_file is not None:
        amber_client = AmberV2Client(profile_name=amber_license_id, license_file=amber_license_file)
    else:
        secret_dict = get_secrets()
        license_profile = secret_dict.get(amber_license_id, None)
        amber_client = AmberV2Client(profile=license_profile, verify=False)
    return amber_client
