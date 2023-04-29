#!/usr/bin/env python
# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

from __future__ import print_function

import os
import sys

# Let the user know which Python is picked up to run the tests.
print(
    'Using Python version "%s" at "%s"'
    % (".".join(str(i) for i in sys.version_info[0:3]), sys.executable)
)

# prepend tank_vendor location to PYTHONPATH to make sure we are running
# the tests against the vendor libs, not local libs on the machine
core_python_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "python")
)
print("Adding tank location to python_path: %s" % core_python_path)
sys.path = [core_python_path] + sys.path

# prepend tank_vendor location to PYTHONPATH to make sure we are running
# the tests against the vendor libs, not local libs on the machine
test_python_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "python")
)
print("Adding tests/python location to python_path: %s" % test_python_path)
sys.path = [test_python_path] + sys.path

test_python_path = os.path.join(test_python_path, "third_party")
print(
    "Adding tests/python/third_party location to python_path: %s"
    % test_python_path
)
sys.path = [test_python_path] + sys.path
