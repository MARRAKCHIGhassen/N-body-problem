# -*- coding: utf-8 -*-
"""node Module

Nodes are the boxes that contain different bodies.

Name
-------
vector

Author
-------
Ghassen MARRAKCHI
Fatma MARZOUGUI

Release
-------
0.1

Reference
-------
rosettacode.org
"""










#-------------------------------------------------------------------------------------------------------------------



# Importing Global Libraries
import numpy as np
from math import sqrt

# Import custom libraries
import NBody_problem.utils.config as config
import NBody_problem.area.space.vector as vector

class Node:
    def __init__(self, bodies_number, arete, geometrical_center):
        # Initializing the geometry
        self.geometrical_center = vector.Vector()
        self.arete = arete
        self.limits = self._set_limits()

        # Initializing bodies
        self.bodies_number = bodies_number
        self.childs = self._set_bodies()

        # Initializing specific Node features
        self.center_of_mass = 0
        self.total_mass = 0

    def _set_limits(self):
        # Initialize Array
        limits = dict()
        
        # X limits
        limits['x_low_lim'] = vector.Vector(self.geometrical_center.x + (self.arete / 2),
                                            self.geometrical_center.y,
                                            self.geometrical_center.z)

        limits['x_high_lim'] = vector.Vector(self.geometrical_center.x - (self.arete / 2),
                                            self.geometrical_center.y,
                                            self.geometrical_center.z)



        # Y limits
        limits['y_low_lim'] = vector.Vector(self.geometrical_center.x,
                                            self.geometrical_center.y + (self.arete / 2),
                                            self.geometrical_center.z)
                                            
        limits['y_high_lim'] = vector.Vector(self.geometrical_center.x,
                                            self.geometrical_center.y - (self.arete / 2),
                                            self.geometrical_center.z)


        # Z limits
        limits['z_low_lim'] = vector.Vector(self.geometrical_center.x,
                                            self.geometrical_center.y,
                                            self.geometrical_center.z - (self.arete / 2))
                                            
        limits['z_high_lim'] = vector.Vector(self.geometrical_center.x,
                                            self.geometrical_center.y,
                                            self.geometrical_center.z  + (self.arete / 2))

        return limits

    def _set_bodies(self):
        corners = 0
        center = 0
        return (corners, center)

    def inside(self, p):
        """
        given coordinate is inside the bounding box
        input: p is an array of x, y, z
        output: True or False
        """
        if (p[0] < self.xlow or p[0] > self.xhigh or p[1] < self.ylow or p[1] > self.yhigh or p[2] < self.zlow or p[2] > self.zhigh):
            return False
        else:
            return True
        
    def middle(self):
        """
        returns center of bounding box
        """
        return np.array([((self.xlow + self.xhigh))/2., (self.ylow + self.yhigh)/2., (self.zlow + self.zhigh)/2.])
    
    def bounds(self):
        """
        returns min/max values of the bounding box
        """
        return np.array([self.bb.min(), self.bb.max()])
