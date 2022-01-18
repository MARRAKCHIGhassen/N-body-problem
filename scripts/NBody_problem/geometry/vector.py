# -*- coding: utf-8 -*-
"""Vector Module

Vectors will be used to represent position of different bodies.

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
import math

# Import custom libraries
import NBody_problem.utils.log as log



class Vector:
    def __init__(self, x=0, y=0, z=0):
        """Vector Constructor

        Parameters
        ----------
        x : float
            Position in the width scale.
        
        y : float
            Position in the depth scale.
    
        z : float
            Position in the height scale.
        """

        #------------------------------------------------
        

        log.log("STARTED", "vector.py", "__init__")

        self.x = x
        self.y = y
        self.z = z

        log.log("ENDED", "vector.py", "__init__")


    def __add__(self, other):
        """Add two vectors.

        Parameters
        ----------
        other : vector
            Vector to add.
        

        Returns
        -------
        vector : vector
            Vector addition result.
        """

        #------------------------------------------------
        
        
        log.log("STARTED", "vector.py", "__add__")

        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)


    def __sub__(self, other):
        """Subtraction of two vectors.

        Parameters
        ----------
        other : vector
            Vector to add.
        

        Returns
        -------
        vector : vector
            Vector Subtraction result.
        """

        #------------------------------------------------
        
        
        log.log("STARTED", "vector.py", "__sub__")

        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)


    def __mul__(self, other):
        """Scalar multiplication of the vector.

        Parameters
        ----------
        other : float
            Scalar to multiply the vector with.
        

        Returns
        -------
        vector : vector
            Vector scalar multiplication result.
        """

        #------------------------------------------------
        
        
        log.log("STARTED", "vector.py", "__mul__")

        return Vector(self.x * other, self.y * other, self.z * other)


    def __div__(self, other):
        """Scalar division of the vector.

        Parameters
        ----------
        other : float
            Scalar to divide the vector with.
        

        Returns
        -------
        vector : vector
            Vector scalar division result.
        """

        #------------------------------------------------
        
        
        log.log("STARTED", "vector.py", "__div__")

        return Vector(self.x / other, self.y / other, self.z / other)


    def __eq__(self, other):
        """Verify the if two vectors are equal.

        Parameters
        ----------
        other : vector
            Vector to verify with.
        

        Returns
        -------
        bool : bool
            True if the two vectors are equal, False else.
        """

        #------------------------------------------------
        
        
        log.log("STARTED", "vector.py", "__eq__")

        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return False


    def __ne__(self, other):
        """Verify the if two vectors are NOT equal.

        Parameters
        ----------
        other : vector
            Vector to verify with.
        

        Returns
        -------
        bool : bool
            True if the two vectors are NOT equal, False else.
        """

        #------------------------------------------------
        
        
        log.log("STARTED", "vector.py", "__ne__")

        return not self.__eq__(other)


    def __str__(self):
        """convert the vector to string.

        Returns
        -------
        str : str
            Vector converted & formatted to a string.
        """

        #------------------------------------------------
        
        
        log.log("STARTED", "vector.py", "__str__")

        return '({x}, {y}, {z})'.format(x=self.x, y=self.y, z=self.z)


    def abs(self):
        """Return the norm of the vector.

        Returns
        -------
        float : float
            Norm of the vector.
        """

        #------------------------------------------------
        
        
        log.log("STARTED", "vector.py", "abs")

        return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)
    

    def distance(vect_1, vect_2):
        """calculate distance between two vectors

        Parameters
        ----------
        vect_1 : vector
            the first vector.

        vect_2 : vector
            the second vector.
        
        Returns
        -------
        float : float
            distance between two vectors.
        """

        #------------------------------------------------
        

        log.log("STARTED", "vector.py", "distance")

        return math.sqrt((vect_1.x - vect_2.x)**2 + (vect_1.y - vect_2.y)**2 + (vect_1.z - vect_2.z)**2)

    
