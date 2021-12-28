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



# Importing Global Libraries
import os

# Import custom libraries
from configparser import ConfigParser
import NBody_problem.utils.log as log
import NBody_problem.utils.settings as settings
import NBody_problem.area.body as body
import NBody_problem.geometry.vector as vector



# Main Functions
def configure():
	"""Get the user confirmation about config.ini before integrate configuration"""
	
	#------------------------------------------------ 
	

	log.log("STARTED", "config.py", "configure")
	
	# print file structure
	print("---------------- Please verify the config.ini structure")
	print("---------------- You can use the .config/config_sample")
	print("---------------- If you make modification into the above file, please make sure to save changes under .config/config.ini")
	print_config_file_struct()
	print('\n \n')

	# Reading the file name
	confirmation = False
	input_str = ""
	while ((input_str != 'y') and (input_str != 'n')):
		input_str = input("Do you confirm config.ini configuration si done ? ([y]/n): ")
		if input_str == 'y' :
			confirmation = True

	# Verification
	if confirmation == False :
		return 
	
	integrate_configuration()

	log.log("ENDED", "config.py", "configure")

def update_config():
	"""Update config.ini file."""
	
	#------------------------------------------------ 
	

	log.log("STARTED", "config.py", "update_config")
	
	# print file structure
	print("---------------- You requested updating configuration")
	print("---------------- You can abort if there are no changes made into config.ini")
	print_config_file_struct()
	print('\n \n')

	# Reading the file name
	confirmation = False
	input_str = ""
	while ((input_str != 'y') and (input_str != 'n')):
		input_str = input("Do you confirm updating config.ini ? ([y]/n): ")
		if input_str == 'y' :
			confirmation = True

	# Verification
	if confirmation == False :
		return 
	
	integrate_configuration()

	log.log("ENDED", "config.py", "update_config")

def integrate_configuration():
	"""Integrate configuration from config.ini file to the main program flow."""
	
	#------------------------------------------------ 
	

	log.log("STARTED", "config.py", "integrate_configuration")
	
	# get the configuration
	config = ConfigParser()
	config.read(settings.CONFIG_PATH)
	
	# Printing paramteters
	section = dict(config['program_param'])
	try :
		# Verify if it is correctly input
		settings.Interface = int(section['interface'])
	except :
		print('Erreur dans la conversion de interface')
		return

	# Environlent Parameters
	section = dict(config['env_param'])
	
	# dimension
	try :
		# Verify if it is correctly input
		settings.Dimension = int(section['dimension'])
	except :
		print('Erreur dans la conversion de dimension')
		return

	# arete
	try :
		# Verify if it is correctly input
		settings.Arete = float(section['arete'])
	except :
		print('Erreur dans la conversion de arete')
		return

	# gravitation
	try :
		# Verify if it is correctly input
		settings.Gravitation = float(section['gravitation'])
	except :
		print('Erreur dans la conversion de gravitation')
		return

	# theta
	try :
		# Verify if it is correctly input
		settings.Theta = float(section['theta'])
	except :
		print('Erreur dans la conversion de theta')
		return

	# softening
	try :
		# Verify if it is correctly input
		settings.Softening = float(section['softening'])
	except :
		print('Erreur dans la conversion de softening')
		return


	# Simulation Parameters
	section = dict(config['sim_param'])

	# number_bodies
	try :
		# Verify if it is correctly input
		settings.Number_bodies = int(section['number_bodies'])
	except :
		print('Erreur dans la conversion de number_bodies')
		return

	# end_time
	try :
		# Verify if it is correctly input
		settings.End_time = float(section['end_time'])
	except :
		print('Erreur dans la conversion de end_time')
		return

	# timestep
	try :
		# Verify if it is correctly input
		settings.Timestep = float(section['timestep'])
	except :
		print('Erreur dans la conversion de timestep')
		return

	
	# Bodies
	settings.N_bodies = []
	index = 0
	while True :
		try :
			# Verify if the section exists
			section = dict(config['body_' + str(index)])
		except :
			return

		# Create new body
		new_body = body.Body(index)

		# Mass
		try :
			# Verify if it is correctly input
			new_body.mass = float(section['mass'])
		except :
			print('Erreur dans la conversion de mass')
			return

		# Position
		new_body.position = vector.Vector()
		try :
			# Verify if it is correctly input
			new_body.position.x = float(section['position_x'])
		except :
			print('Erreur dans la conversion de position x')
			return

		try :
			# Verify if it is correctly input
			new_body.position.y = float(section['position_y'])
		except :
			print('Erreur dans la conversion de position y')
			return

		try :
			# Verify if it is correctly input
			new_body.position.z = float(section['position_z'])
		except :
			print('Erreur dans la conversion de position z')
			return

		# Velocity
		new_body.velocity = vector.Vector()
		try :
			# Verify if it is correctly input
			new_body.velocity.x = float(section['velocity_x'])
		except :
			print('Erreur dans la conversion de velocity x')
			return

		try :
			# Verify if it is correctly input
			new_body.velocity.y = float(section['velocity_y'])
		except :
			print('Erreur dans la conversion de velocity y')
			return

		try :
			# Verify if it is correctly input
			new_body.velocity.z = float(section['velocity_z'])
		except :
			print('Erreur dans la conversion de velocity z')
			return

		# Acceleration
		new_body.acceleration = vector.Vector()
		try :
			# Verify if it is correctly input
			new_body.acceleration.x = float(section['acceleration_x'])
		except :
			print('Erreur dans la conversion de acceleration x')
			return

		try :
			# Verify if it is correctly input
			new_body.acceleration.y = float(section['acceleration_y'])
		except :
			print('Erreur dans la conversion de acceleration y')
			return

		try :
			# Verify if it is correctly input
			new_body.acceleration.z = float(section['acceleration_z'])
		except :
			print('Erreur dans la conversion de acceleration z')
			return

		# Add the body
		settings.N_bodies.append(new_body)
		settings.Positions.append(new_body.position)

		# Next
		index += 1

def print_config_file_struct():
	"""Prints the .config/config_sample file content"""
	
	#------------------------------------------------ 
	


	print('##########################')
	print('##########################')
	print('FILE STRUCTURE ###########')
	with open(os.path.join('.config', 'config_sample'), 'r') as f:
		print(f.read())
	print('##########################')
	print('##########################')

