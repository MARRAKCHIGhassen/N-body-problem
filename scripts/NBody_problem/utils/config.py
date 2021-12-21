# -*- coding: utf-8 -*-
"""Configuration Module.

Get and storage configurations related to preferences and simulation in 'config.ini'.

Sections
-------
simulation
	Contain the configuration related to the problem (Physical informations).

Name
-------
config

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
from configparser import ConfigParser
import NBody_problem.utils.log as log
import NBody_problem.utils.settings as settings



# Main Functions
def configure():
	"""Initialize config.ini file."""
	
	#------------------------------------------------ 
	

	log.log("STARTED", "config.py", "configure")
	
	# configurator
	config = ConfigParser()
	
	# Add simulation section
	config.add_section("simulation")

	# Laboratory Informations
	print("---------------- Problem related informations")

	# Add number of bodies
	bodies_number = __read_bodies_number()
	config.set("simulation", "bodies_number", str(bodies_number))

	# Add space width (x)
	space_width = __read_space_width()
	config.set("simulation", "space_width", str(space_width))

	# Add space height (y)
	space_height = __read_space_height()
	config.set("simulation", "space_height", str(space_height))

	# Add space depth (z)
	space_depth = __read_space_depth()
	config.set("simulation", "space_depth", str(space_depth))

	# save in config.ini
	__save_config(config)

	log.log("ENDED", "config.py", "configure")


def update_config():
	"""Update config.ini file."""
	
	#------------------------------------------------ 
	

	log.log("STARTED", "config.py", "update_config")
	
	# configurator
	config = __get_current_config()
	
	# Update number of bodies
	bodies_number = __print_current_bodies_number(config)
	answer = input("Do you want to change the number of bodies ? (y : yes / other : no) : ")
	if answer == 'y':
		bodies_number = __read_bodies_number()

	# Update space width
	space_width = __print_current_space_width(config)
	answer = input("Do you want to change the width of the space ? (y : yes / other : no) : ")
	if answer == 'y':
		space_width = __read_space_width()


	# Update space height
	space_height = __print_current_space_height(config)
	answer = input("Do you want to change the height of the space ? (y : yes / other : no) : ")
	if answer == 'y':
		space_height = __read_space_height()


	# Update space depth
	space_depth = __print_current_space_depth(config)
	answer = input("Do you want to change the depth of the space ? (y : yes / other : no) : ")
	if answer == 'y':
		space_depth = __read_space_depth()


	# Update simulation section
	config.set("simulation", "bodies_number", str(bodies_number))
	config.set("simulation", "space_width", str(space_width))
	config.set("simulation", "space_height", str(space_height))
	config.set("simulation", "space_depth", str(space_depth))

	# save in config.ini
	__save_config(config)


	log.log("ENDED", "config.py", "update_config")



# Getters
def get_bodies_number(config=None):
	"""return 'bodies_number' value from 'simulation' section in the file config.ini.
	
	Parameters
    ----------
    config : ConfigParser, optional
        Configurator.

	Returns
    -------
    str : str
        The value of 'bodies_number' from 'simulation' section.
	"""
	
	#------------------------------------------------ 


	log.log("STARTED", "config.py", "get_bodies_number")
	
	# configurator
	if config == None :
		config = __get_current_config()
	
	simulation = dict(config['simulation'])

	log.log("ENDED", "config.py", "get_bodies_number")

	return simulation['bodies_number']


def get_space_width(config=None):
	"""return 'space_width' value from 'simulation' section in the file config.ini.
	
	Parameters
    ----------
    config : ConfigParser, optional
        Configurator.

	Returns
    -------
    str : str
        The value of 'space_width' from 'simulation' section.
	"""
	
	#------------------------------------------------ 


	log.log("STARTED", "config.py", "get_space_width")
	
	# configurator
	if config == None :
		config = __get_current_config()
	
	simulation = dict(config['simulation'])

	log.log("ENDED", "config.py", "get_space_width")

	return simulation['space_width']


def get_space_height(config=None):
	"""return 'space_height' value from 'simulation' section in the file config.ini.
	
	Parameters
    ----------
    config : ConfigParser, optional
        Configurator.

	Returns
    -------
    str : str
        The value of 'space_height' from 'simulation' section.
	"""
	
	#------------------------------------------------ 


	log.log("STARTED", "config.py", "get_space_height")
	
	# configurator
	if config == None :
		config = __get_current_config()
	
	simulation = dict(config['simulation'])

	log.log("ENDED", "config.py", "get_space_height")

	return simulation['space_height']


def get_space_depth(config=None):
	"""return 'space_depth' value from 'simulation' section in the file config.ini.
	
	Parameters
    ----------
    config : ConfigParser, optional
        Configurator.

	Returns
    -------
    str : str
        The value of 'space_depth' from 'simulation' section.
	"""
	
	#------------------------------------------------ 


	log.log("STARTED", "config.py", "get_space_depth")
	
	# configurator
	if config == None :
		config = __get_current_config()
	
	simulation = dict(config['simulation'])

	log.log("ENDED", "config.py", "get_space_depth")

	return simulation['space_depth']



# Private functions
def __get_current_config() :
	"""Return current configuration.

	Returns
    -------
    config : ConfigParser
        Configurator.
	"""
	
	#------------------------------------------------ 


	log.log("STARTED", "config.py", "__get_current_config")
	
	# configurator
	config = ConfigParser()
	config.read(settings.CONFIG_PATH)

	log.log("ENDED", "config.py", "__get_current_config")

	return config


def __print_current_bodies_number(config) :
	"""Print current number of bodies

	Parameters
    ----------
    config : ConfigParser
        Configurator.
	
	Returns
    -------
    bodies_number : str
        The current number of bodies.
	"""
	
	#------------------------------------------------ 


	log.log("STARTED", "config.py", "__print_current_bodies_number")
	
	bodies_number = get_bodies_number(config)
	print("-------------")
	print("Number of bodies : ", bodies_number)
	print("-------------")

	log.log("ENDED", "config.py", "__print_current_bodies_number")

	return bodies_number


def __print_current_space_width(config) :
	"""Print current width of the space

	Parameters
    ----------
    config : ConfigParser
        Configurator.
	
	Returns
    -------
    space_width : str
        The current width of the space.
	"""
	
	#------------------------------------------------ 


	log.log("STARTED", "config.py", "__print_current_space_width")
	
	space_width = get_space_width(config)
	print("-------------")
	print("space_width : ", space_width)
	print("-------------")

	log.log("ENDED", "config.py", "__print_current_space_width")

	return space_width


def __print_current_space_height(config) :
	"""Print current height of the space

	Parameters
    ----------
    config : ConfigParser
        Configurator.
	
	Returns
    -------
    space_height : str
        The current height of the space.
	"""
	
	#------------------------------------------------ 


	log.log("STARTED", "config.py", "__print_current_space_height")
	
	space_height = get_space_height(config)
	print("-------------")
	print("space_height : ", space_height)
	print("-------------")

	log.log("ENDED", "config.py", "__print_current_space_height")

	return space_height


def __print_current_space_depth(config) :
	"""Print current depth of the space

	Parameters
    ----------
    config : ConfigParser
        Configurator.
	
	Returns
    -------
    space_depth : str
        The current depth of the space.
	"""
	
	#------------------------------------------------ 


	log.log("STARTED", "config.py", "__print_current_space_depth")
	
	space_depth = get_space_depth(config)
	print("-------------")
	print("space_depth : ", space_depth)
	print("-------------")

	log.log("ENDED", "config.py", "__print_current_space_depth")

	return space_depth


def __read_bodies_number() :
	"""Read number of bodies given by the user

	Returns
    -------
    bodies_number : int
        The number of bodies in the space.
	"""
	
	#------------------------------------------------ 


	log.log("STARTED", "config.py", "__read_bodies_number")

	bodies_number = 0
	while (bodies_number <= 1):
		try :
			bodies_number = int(input("Give the number bodies within the simulation (>= 2) : "))
			
		except :
			print("Given value must be an integer")
	
	log.log("ENDED", "config.py", "__read_bodies_number")

	return bodies_number


def __read_space_width() :
	"""Read the width of space given by the user

	Returns
    -------
    space_width : float
        The width of the space.
	"""
	
	#------------------------------------------------ 


	log.log("STARTED", "config.py", "__read_space_width")

	space_width = 0
	while (space_width <= 9.0):
		try :
			space_width = float(input("Give the width of the space of the simulation (>= 10.0) : "))
			
		except :
			print("Given value must be a float")
	
	log.log("ENDED", "config.py", "__read_space_width")

	return space_width


def __read_space_height() :
	"""Read the height of space given by the user

	Returns
    -------
    space_height : float
        The height of the space.
	"""
	
	#------------------------------------------------ 


	log.log("STARTED", "config.py", "__read_space_height")

	space_height = 0
	while (space_height <= 9.0):
		try :
			space_height = float(input("Give the height of the space of the simulation (>= 10.0) : "))
			
		except :
			print("Given value must be a float")
	
	log.log("ENDED", "config.py", "__read_space_height")

	return space_height


def __read_space_depth() :
	"""Read the depth of space given by the user

	Returns
    -------
    space_depth : float
        The depth of the space.
	"""
	
	#------------------------------------------------ 


	log.log("STARTED", "config.py", "__read_space_depth")

	space_depth = 0
	while (space_depth <= 9.0):
		try :
			space_depth = float(input("Give the depth of the space of the simulation (>= 10.0) : "))
			
		except :
			print("Given value must be a float")
	
	log.log("ENDED", "config.py", "__read_space_depth")

	return space_depth


def __save_config(config):
	"""Save the configuration

	Parameters
    ----------
	config : ConfigParser
		Configurator.
	"""
	
	#------------------------------------------------ 


	log.log("STARTED", "config.py", "__save_config")
	print(settings.CONFIG)
	if not settings.CONFIG :
		os.system("mkdir {}".format(settings.CONFIG_DIR_PATH))
		os.system("touch {}".format(settings.CONFIG_PATH))
	
	settings.CONFIG = True

	with open(settings.CONFIG_PATH, 'w') as configFile:
		config.write(configFile)
	
	log.log("ENDED", "config.py", "__save_config")


