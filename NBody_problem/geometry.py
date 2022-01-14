# -*- coding: utf-8 -*-


import math


class Rectangle:
    """Un rectangle centré à (center_x, center_y) d'arete arete"""

    def __init__(self, center_x, center_y, arete):
        self.center_x, self.center_y = center_x, center_y
        self.arete = arete
        self.west_edge, self.east_edge = center_x - arete/2, center_x + arete/2
        self.north_edge, self.south_edge = center_y - arete/2, center_y + arete/2

    def __repr__(self):
        return str((self.west_edge, self.east_edge, self.north_edge,
                self.south_edge))

    def __str__(self):
        return '({:.2f}, {:.2f}, {:.2f}, {:.2f})'.format(self.west_edge,
                    self.north_edge, self.east_edge, self.south_edge)

    def contains(self, point):
        """Is point (a Point object or (x,y) tuple) inside this Rect?"""

        try:
            point_x, point_y = point.x, point.y
        except AttributeError:
            point_x, point_y = point

        return (point_x >= self.west_edge and
                point_x <  self.east_edge and
                point_y >= self.north_edge and
                point_y < self.south_edge)

## VECTOR
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
        
        self.x = x
        self.y = y
        self.z = z

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
        
        return not self.__eq__(other)


    def __str__(self):
        """convert the vector to string.

        Returns
        -------
        str : str
            Vector converted & formatted to a string.
        """

        #------------------------------------------------
        
        return '({x}, {y}, {z})'.format(x=self.x, y=self.y, z=self.z)


    def abs(self):
        """Return the norm of the vector.

        Returns
        -------
        float : float
            Norm of the vector.
        """

        #------------------------------------------------
        
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
        
        return math.sqrt((vect_1.x - vect_2.x)**2 + (vect_1.y - vect_2.y)**2 + (vect_1.z - vect_2.z)**2)

    
