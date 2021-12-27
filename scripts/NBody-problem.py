# -*- coding: utf-8 -*-
"""NBody problem simulation

A mini project done for the data structure subject, Master 1 in computer Science, @Galilee Institute - Sorbonne Paris Nord - Paris, FRANCE.

Name
-------
NBody Problem

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
import sys

# Import custom libraries
import NBody_problem.utils.log as log
import NBody_problem.utils.config as config
import NBody_problem.utils.args as args

import NBody_problem.simulation.simulation as sim


def launch():
	"""Main program launch."""
	
	#------------------------------------------------
	
	log.log("STARTED", "NBody-problem.py", "launch")
	
	# Bodies
	NBodies = config.get_bodies()

	# Launch simulation
	sim.launch_simulation(NBodies)
	
	log.log("ENDED", "NBody-problem.py", "launch")



# Main program start
if __name__ == "__main__":

	log.start_log()
	log.log("STARTED", "NBody-problem.py", "__main__")

	# Verify arguments
	if args.launch(sys.argv) :
		launch()

	log.log("ENDED", "NBody-problem.py", "__main__")

