# -*- coding: utf-8 -*-
"""Help Module.

Name
-------
helper

Author
-------
Ghassen MARRAKCHI
Fatma MARZOUGUI

Release
-------
0.1
"""










#-------------------------------------------------------------------------------------------------------------------



# Importing Global Libraries

# Import custom libraries
import NBody_problem.utils.config as config



def print_help():
    """Print the help"""

    #------------------------------------------------
    
    print("-------------------HELP---------------")
    print("--version : Print version")
    print("--author  : Print project authors")
    print("--help    : Print help")
    print("--config  : Launch configuration")
    print("-------------------------------------")

    config.print_config_file_struct()
