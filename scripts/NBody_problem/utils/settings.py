# -*- coding: utf-8 -*-

## PATHS
import os
CONFIG_DIR_PATH = "./../.config"
CONFIG_PATH = "./../.config/config.ini"
LOG_PATH = "./../log/log"
LOG_DIR_PATH = "./../log"

# VERIFICATION
CONFIG = os.path.isfile(CONFIG_PATH)

MAX_BODIES = 0
NBodies = 0
GRAVITATION = 1.0
THETA = 0.5