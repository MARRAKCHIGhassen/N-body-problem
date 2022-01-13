# -*- coding: utf-8 -*-
"""Arguments Management Module.

Make the program respond according to the given arguments.

Name
-------
args

Author
-------
Ghassen MARRAKCHI
Fatma MARZOUGUI

Release
-------
0.1
"""










#-------------------------------------------------------------------------------------------------------------------



# Importing libraries
import NBody_problem.utils.log as log
import NBody_problem.utils.settings as settings
import NBody_problem.utils.config as config
import NBody_problem.utils.helper as help



def launch(args) :
    """Verify whether the program can be launched or not.

    Parameters
    ----------
    args : sys.argv
        Arguments given to the main program.
    
    Returns
    -------
    bool : bool
        True if the main program will launched, False else.
    """

    #------------------------------------------------
    

    log.log("STARTED", "args.py", "launch")
    
    length = len(args)
    
    if length > 2 : # Verify much arguments
        print("Too many arguments")

        log.log("ENDED", "args.py", "launch")

        return False
    
    elif length == 1 : # Normal launch
        if settings.CONFIG == False :    # Verify configuration done
            print("You have to configure the program first")
            print("You can use '--config' argument")
            return False

        log.log("ENDED", "args.py", "launch")
        return True
    

    # To minimize access
    argument = args[1]

    if argument == '--version' :
        print('Version : 0.1')

    elif argument == '--author' :
        print('Author : Ghassen MARRAKCHI')

    elif argument == '--help' :
        help.print_help()

    elif argument == '--config' :
        if settings.CONFIG == False :    # Verify configuration done
            config.configure()
        else :
            config.update_config()

    log.log("ENDED", "args.py", "launch")
    
    return False

