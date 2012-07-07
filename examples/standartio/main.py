#!/usr/bin/python3

import sys
import os
FILE_DIR  = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(FILE_DIR,"..",".."))

from pyircclient.clients import StandartioBotLauncher


# exemple de changement des paramètres par default du launcher
launcher = StandartioBotLauncher(exec_name="./test.py", exec_params=[])
launcher.run()

