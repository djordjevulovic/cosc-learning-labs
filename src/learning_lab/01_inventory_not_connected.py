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

''' Sample usage of function 'inventory_not_connected' to show which devices are mounted, but not connected.

    Print the function's documentation then invoke the function and print the output.
'''

from __future__ import print_function as _print_function
from basics.inventory import inventory_not_connected
from basics.render import print_table
from pydoc import render_doc as doc
from pydoc import plain

def main():
    print(plain(doc(inventory_not_connected)))
    print("inventory_not_connected()")
    print_table(inventory_not_connected(), headers='device-name')
    
if __name__ == "__main__":
    main()