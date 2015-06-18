# Copyright 2015 Cisco Systems, Inc.
# 
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

from __future__ import print_function
from unittest.case import TestCase
from basics.inventory import capability_discovery
from unittest import main
from helpers import inventory_connect, inventory_purge

class Test(TestCase):

    def setUp(self):
        """
        Connect every network device configured in the settings.
        """
        inventory_purge()
        inventory_connect()
        

    def test_capability_discovery(self):
        discoveries = capability_discovery()
        self.assertTrue(discoveries, "Expected one or more capable devices.")
        device_names = set([discovered.device_name for discovered in discoveries])
        capability_names = set([discovered.capability.name for discovered in discoveries])
        capability_namespaces = set([discovered.capability.namespace for discovered in discoveries])
        capability_revisions = set([discovered.capability.revision for discovered in discoveries])
        capabilities = set([discovered.capability for discovered in discoveries])
        
        for discovered in discoveries[0:10]:
            rediscover = capability_discovery(
                device_name=discovered.device_name,
                capability_name=discovered.capability.name,
                capability_ns=discovered.capability.namespace,
                capability_revision=discovered.capability.revision)
            self.assertEqual(1, len(rediscover), "Expected discovery of %s" % str(discovered))
            self.assertEqual(discovered, rediscover[0])

        for device_name in sorted(device_names)[0:10]:
            rediscover = capability_discovery(device_name=device_name)
            self.assertTrue(rediscover, "Expected device to have capabilities: %s" % device_name)

        for capability_name in sorted(capability_names)[0:10]:
            rediscover = capability_discovery(capability_name=capability_name)
            self.assertTrue(rediscover, "Expected discovery of capability by name %s" % capability_name)

        for capability_namespace in sorted(capability_namespaces)[0:10]:
            rediscover = capability_discovery(capability_ns=capability_namespace)
            self.assertTrue(rediscover, "Expected discovery of capability by name-space %s" % capability_namespace)

        for capability_revision in sorted(capability_revisions)[0:10]:
            rediscover = capability_discovery(capability_revision=capability_revision)
            self.assertTrue(rediscover, "Expected discovery of capability by revision %s" % capability_revision)

        for capability in sorted(capabilities)[0:10]:
            rediscover = capability_discovery(capability_name=capability.name,capability_ns=capability.namespace,capability_revision=capability.revision)
            self.assertTrue(rediscover, "Expected discovery of capability %s" % str(capability))
            self.assertEqual(capability, rediscover[0].capability)

if __name__ == '__main__':
    main()
