#!/usr/bin/env python2.7

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

""" 
Demonstrate how to obtain and navigate static routes in JSON representation.

Introduce function 'static_route_json'.
Print the function's documentation.

Determine which network devices have 'static route' capability.
Select any one of these network devices.
Select a different network device when no static routes are found.

Apply the function to the selected network device:
- to obtain all static routes.
- to obtain one specific static route.

Demonstrate the navigation of the 'static route' data structure.
Print the JSON representation of one static route.
"""

from __future__ import print_function
from collections import OrderedDict
from pydoc import plain
from pydoc import render_doc as doc
import os
from ipaddress import ip_network
from basics.render import print_rich
from basics.interpreter import sys_exit
from basics.routes import static_route_json, inventory_static_route
import json
from importlib import import_module
static_route_fixture = import_module('learning_lab.04_static_route_fixture')

def demonstrate(device_name):
    """
    Apply function 'static_route_json' to the specified device to obtain all
    static routes and one specifiec static route.
    """
    print('Request all static routes.')
    print('static_route_json(%s)' % device_name)
    route_list = static_route_json(device_name)
    if not route_list:
        print(None)
        return False
    
    print_rich([OrderedDict([
            ("device", device_name),
            ("destination", "%s/%s" % (route['prefix'], route['prefix-length'])),
            ("next-hop", route['vrf-route']['vrf-next-hops']['next-hop-address'][0]['next-hop-address'])
        ]) for route in route_list
    ])
    print()
    
    print('Request a specific static route.')
    route = route_list[0]
    destination_network = ip_network("%s/%s" % (route['prefix'], route['prefix-length']))
    print('static_route_json(%s, %s)' % (device_name, destination_network))
    route = static_route_json(device_name, destination_network)
    print(json.dumps(route, indent=2, sort_keys=True))
    return True

def main():
    """ 
    Print function documentation then demonstrate function usage on any one device.
     
    Repeat for another device if no 'static route' is configured.
    """
    print(plain(doc(static_route_json)))

    print('Determine which devices are capable.')
    print('inventory_static_route()')
    inventory = inventory_static_route()
    if not inventory:
        print(None)
        print("There are no 'static route' capable devices. Demonstration cancelled.")
    else:
        print_rich(inventory)
        print()
        for device_name in inventory:
            if demonstrate(device_name):
                return os.EX_OK
        print("There are no devices with a 'static route' configured. Demonstration cancelled.")
    return os.EX_TEMPFAIL

if __name__ == "__main__":
    sys_exit(main())
