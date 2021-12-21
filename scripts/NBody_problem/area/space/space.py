# -*- coding: utf-8 -*-
"""space Module

The space is the Octree representing each nodes.

Name
-------
space

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
import math

# Import custom libraries
import NBody_problem.utils.config as config

import NBody_problem.area.space.node as node


class Space:
    def __init__(self):
        # Collecte de la configuration
        width = config.get_space_width()
        height = config.get_space_height()
        depth = config.get_space_depth()
        
        self.bodies_number = config.get_bodies_number()
        self.theta = 0.5
        self.gravitation = 1.0

        # Initialization of the root
        self.root = node.Node(self.bodies_number, arete, center)
        
    


    