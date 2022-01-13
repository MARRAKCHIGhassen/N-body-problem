# -*- coding: utf-8 -*-

## CONSTANTS
## PATHS
import os
CONFIG_DIR_PATH = "./../.config"
CONFIG_PATH = "./.config/config.ini"
LOG_PATH = "./../log/log"
LOG_DIR_PATH = "./../log"

# VERIFICATION
CONFIG = os.path.isfile(CONFIG_PATH)

# DIMENSION
PLAN = 0
SPACE = 1

# PRINTING
CONSOLE = 0
GUI = 1



## Configuration Parameters
# Interface paramteters
Interface = 0

# Environment Parameters 
Dimension = 0
Arete = 50
Gravitation = 1.0
Theta = 0.5
Softening = 0.1

# Single Node Parameters
Max_bodies = 1

# Simulation Parameters
Number_bodies = 0
End_time = 10.0
Timestep = 0.01



# Simulation Global Variables
N_bodies = []
Positions = []
