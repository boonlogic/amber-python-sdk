from __future__ import absolute_import

import unittest
import os

from boonamber import (
    AmberV2Client,
    ApiException,
)

class TestOauth(unittest.TestCase):
    """Authentication unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOauthRefresh(self):
        """Test Refresh Oauth"""
        license_id = os.getenv('AMBER_TEST_LICENSE_ID')
        license_file = os.getenv('AMBER_TEST_LICENSE_FILE')
        api = AmberV2Client(license_id=license_id, license_file=license_file)
        api.get_version()

        # reset reauth_time to force a refresh oauth
        api.reauth_time = 0
        old_refresh = api.refresh_token
        version = api.get_version()
        assert old_refresh != api.refresh_token

    def testLicenseFile(self):
        """Test License File"""
        import os
        env_file = os.getenv("AMBER_V2_LICENSE_FILE")
        if env_file is not None:
            del os.environ["AMBER_V2_LICENSE_FILE"]

        # test not formatted correctly
        with self.assertRaises(ApiException):
            AmberV2Client(license_file="bad.Amber.license")

        # test doesnt exist
        with self.assertRaises(ApiException):
            AmberV2Client(license_file="bogus.Amber.license")

        if env_file is not None:
            os.environ["AMBER_V2_LICENSE_FILE"] = env_file

    def testLicenseProfile(self):
        """Test License Credentials"""
        import os
        env_id = os.getenv("AMBER_V2_LICENSE_ID")
        if env_id is not None:
            del os.environ["AMBER_V2_LICENSE_ID"]
        env_file = os.getenv("AMBER_V2_LICENSE_FILE")
        if env_file is not None:
            del os.environ["AMBER_V2_LICENSE_FILE"]

        # test non existant id
        with self.assertRaises(ApiException):
            AmberV2Client(license_file="test.Amber.license", license_id="bogus")


        # get a valid server to check credentials
        license_id = os.getenv('AMBER_TEST_LICENSE_ID')
        license_file = os.getenv('AMBER_TEST_LICENSE_FILE')
        api = AmberV2Client(license_id=license_id, license_file=license_file)
        os.environ["AMBER_V2_SERVER"] = api.server
        os.environ["AMBER_V2_LICENSE_KEY"] = api.license
        os.environ["AMBER_V2_SECRET_KEY"] = api.secret
        api = AmberV2Client(license_file="test.Amber.license", license_id="invalid-credentials")

        # should work anyway with valid credentials given in env
        version = api.get_version()
        assert "expert_common" in version.to_dict()

        # test invalid credentials
        del os.environ["AMBER_V2_LICENSE_KEY"]
        del os.environ["AMBER_V2_SECRET_KEY"]
        api = AmberV2Client(license_file="test.Amber.license", license_id="invalid-credentials")
        with self.assertRaises(ApiException):
            api.get_version()

        if env_id is not None:
            os.environ["AMBER_V2_LICENSE_ID"] = env_id
        if env_file is not None:
            os.environ["AMBER_V2_LICENSE_FILE"] = env_file



if __name__ == '__main__':
    unittest.main()
