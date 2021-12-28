# -*- coding: utf-8 -*-
"""Body Module

contains body class.

Name
-------
body

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
import NBody_problem.utils.log as log
import NBody_problem.utils.settings as settings
import NBody_problem.geometry.vector as vector



class Body:
    def __init__(self, id=0, mass=0):
        """Body Constructor

        Parameters
        ----------
        id : int
            ID of the body. It will be used in the nbodies list.
        
        mass : float
            Mass of the body
        """

        #------------------------------------------------
        

        log.log("STARTED", "body.py", "__init__")

        self.id = id
        self.mass = mass
        self.position = vector.Vector(0, 0, 0)
        self.velocity = vector.Vector(0, 0, 0)
        self.acceleration = vector.Vector(0, 0, 0)

        log.log("ENDED", "body.py", "__init__")
    

    def compute(self) :
        """The acceleration being updated, it updates velocity and position."""

        #------------------------------------------------
        

        log.log("STARTED", "body.py", "compute")

        self.position += self.velocity + self.acceleration * 0.5
        self.velocity += self.acceleration

        log.log("ENDED", "body.py", "__init__")


    def __str__(self):
        """convert the body to string.

        Returns
        -------
        str : str
            Body converted & formatted to a string.
        """

        #------------------------------------------------
        
        
        log.log("STARTED", "body.py", "__str__")
        
        body_str = '\n'
        body_str += '([body_{id}]\n)'.format(id=self.id)
        body_str += '(mass         : {mass}\n)'.format(mass=self.mass)
        body_str += '(position     : {position}\n)'.format(position=self.position)
        body_str += '(velocity     : {velocity}\n)'.format(velocity=self.velocity)
        body_str += '(acceleration : {acceleration}\n)'.format(acceleration=self.acceleration)
        body_str += '---\n'

        return body_str

    
