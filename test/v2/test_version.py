from __future__ import absolute_import

import unittest
import os
import os

from boonamber import (
    AmberV2Client
)

class TestVersion(unittest.TestCase):
    """Version unit test stubs"""

    def setUp(self):
        license_id = os.getenv('AMBER_TEST_LICENSE_ID')
        license_file = os.getenv('AMBER_TEST_LICENSE_FILE')
        self.api = AmberV2Client(profile_name=license_id, license_file=license_file)

        self.label = "python:v2:tests-version"

    def tearDown(self):
        pass

    def testVersion(self):
        """Test Version"""
        version = self.api.get_version()
        # make sure all key elements are filled in
        for key in version.attribute_map.keys():
            # TODO: add mongolia to version
            if key == 'mongolia':
                continue
            assert getattr(version, key) != None


if __name__ == '__main__':
    unittest.main()
