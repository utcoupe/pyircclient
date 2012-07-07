#!/usr/bin/python3

import sys
import os
FILE_DIR  = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(FILE_DIR,"..",".."))

from pyircclient.clients import ArduinoBotLauncher


launcher = ArduinoBotLauncher()
launcher.run()
