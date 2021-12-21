# -*- coding: utf-8 -*-
"""Log Module

Name
-------
log

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
import os
from datetime import datetime
import NBody_problem.utils.settings as settings



def start_log() :
	"""Initilize logging process at the begining of the program"""

    #------------------------------------------------
    

	if not os.path.isdir(settings.LOG_DIR_PATH) :
		os.system('mkdir {}'.format(settings.LOG_DIR_PATH))
		os.system('touch {}'.format(settings.LOG_PATH))
	
	elif not os.path.isfile(settings.LOG_PATH) :
		os.system('touch {}'.format(settings.LOG_PATH))
	
	# Impression du début
	_ = "\n\n-------------------------------{} -------------------------------\n".format(datetime.now())
	

	# Open a file with access mode 'a'
	with open(settings.LOG_PATH, "a") as file_object:
		# Append the log
		file_object.write(_)
	
	# print in the terminal
	print(_)


def log(status, file_, function) :
	"""Log of a function (Terminal + Log File).

    Parameters
    ----------
    status : str
        STARTED if the function starts. ENDED if it's its end.
    
	file_ : str
        Python File name.
    
	function : str
        Function name.
    """

    #------------------------------------------------


	_ = "{} {} {} ------------ {}\n".format(datetime.now(), status, file_, function)
	
	# Open a file with access mode 'a'
	with open(settings.LOG_PATH, "a") as file_object:
		# Append the log
		file_object.write(_)
	
	# print in the terminal
	print(_)

