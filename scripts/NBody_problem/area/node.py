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

# Import custom libraries
import NBody_problem.utils.settings as settings
import NBody_problem.geometry.vector as vector
import NBody_problem.geometry.boundary as bound
import NBody_problem.area.body as body

class NodePlan:
    """A class implementing a Node."""

    def __init__(self, rectangle = bound.Rectangle(0, 0, 0, 0), number_children=0):
        """Initialize this node of the Node.

        boundary is a Rect object defining the region from which points are
        placed into this node; max_points is the maximum number of points the
        node can hold before it must divide (branch into four more nodes);
        depth keeps track of how deep into the Node this node lies.

        """
        # Geometry
        self.boundary = rectangle
        self.children = {'NE' : None, 'SE' : None, 'NW' : None, 'SW' : None}
        self.number_children = number_children

        # Bodies
        self.bodies_number = 0
        self.total_mass = 0.0
        self.center_of_mass = vector.Vector(0, 0, 0)
        self.bodies = []
        self.body = body.Body()

        # Leaf Indicator
        self.leaf = False

    def __str__(self):
        """Return a string representation of this node, suitably formatted."""
        sp = ' ' * self.number_children * 2
        s = str(self.boundary) + '\n'
        s += sp + ', '.join(str(body) for body in self.bodies)
        if self.leaf:
            return s
        return s + '\n' + '\n'.join([
                sp + 'nw: ' + str(self.nw), sp + 'ne: ' + str(self.ne),
                sp + 'se: ' + str(self.se), sp + 'sw: ' + str(self.sw)])

    def divide(self):
        """Divide (branch) this node by spawning four children nodes."""

        cx, cy = self.boundary.cx, self.boundary.cy
        w, h = self.boundary.w / 2, self.boundary.h / 2
        # The boundaries of the four children nodes are "northwest",
        # "northeast", "southeast" and "southwest" quadrants within the
        # boundary of the current node.
        self.children['NE'] = NodePlan(bound.Rectangle(cx - w/2, cy - h/2, w, h),
                                    self.number_children + 1)
        self.children['NW'] = NodePlan(bound.Rectangle(cx + w/2, cy - h/2, w, h),
                                    self.number_children + 1)
        self.children['SE'] = NodePlan(bound.Rectangle(cx + w/2, cy + h/2, w, h),
                                    self.number_children + 1)
        self.children['SW'] = NodePlan(bound.Rectangle(cx - w/2, cy + h/2, w, h),
                                    self.number_children + 1)
        self.leaf = False

    def insert(self, body):
        """Try to insert Point point into this Node."""

        if not self.boundary.contains(body):
            # The point does not lie inside boundary: bail.
            return False
        if self.bodies_number < settings.MAX_BODIES:
            # There's room for our point without dividing the Node.
            self.bodies.append(body.id)
            return True

        # No room: divide if necessary, then try the sub-quads.
        if(not self.leaf): #no particles in this node/cell
            self.update_com()

            for _ in self.children:
                if(self.children[_].contains(body)) :
                    self.children[_].insert(body)
                    return True
            
        else:
            self.divide()
            self.update_com()

            for _ in self.children.keys:
                if(self.children[_].contains(body)) :
                    self.children[_].insert(body)
                    return True

    
        return False

    def update_com(self):
        """
        updates center of mass. p self-explanatory
        """
        self.center_of_mass = vector.Vector(0, 0, 0)
        for body in self.bodies :
            self.center_of_mass.x = body.position.x * body.mass / self.total_mass
            self.center_of_mass.y = body.position.y * body.mass / self.total_mass
            self.center_of_mass.z = body.position.z * body.mass / self.total_mass
        
        return 

    def query(self, boundary, found_bodies):
        """Find the points in the Node that lie within boundary."""

        if not self.boundary.intersects(boundary):
            # If the domain of this node does not intersect the search
            # region, we don't need to look in it for points.
            return False

        # Search this node's points to see if they lie within boundary ...
        for body in self.bodies:
            if boundary.contains(body):
                found_bodies.append(body)
        # ... and if this node has children, search them too.
        if not self.leaf:
            self.children['NE'].query(boundary, found_bodies)
            self.children['NW'].query(boundary, found_bodies)
            self.children['SE'].query(boundary, found_bodies)
            self.children['SW'].query(boundary, found_bodies)
        return found_bodies


    def query_circle(self, boundary, geometrical_center, radius, found_bodies):
        """Find the points in the Node that lie within radius of centre.

        boundary is a Rect object (a square) that bounds the search circle.
        There is no need to call this method directly: use query_radius.

        """

        if not self.boundary.intersects(boundary):
            # If the domain of this node does not intersect the search
            # region, we don't need to look in it for points.
            return False

        # Search this node's points to see if they lie within boundary
        # and also lie within a circle of given radius around the centre point.
        for body in self.bodies:
            if (boundary.contains(body) and
                    body.distance_to(geometrical_center) <= radius):
                found_bodies.append(body)

        # Recurse the search into this node's children.
        if not self.leaf:
            self.children['NE'].query_circle(boundary, geometrical_center, radius, found_bodies)
            self.children['NW'].query_circle(boundary, geometrical_center, radius, found_bodies)
            self.children['SE'].query_circle(boundary, geometrical_center, radius, found_bodies)
            self.children['SW'].query_circle(boundary, geometrical_center, radius, found_bodies)
        return found_bodies

    def query_radius(self, geometrical_center, radius, found_bodies):
        """Find the points in the Node that lie within radius of centre."""

        # First find the square that bounds the search circle as a Rect object.
        boundary = bound.Rectangle(*geometrical_center, 2*radius, 2*radius)
        return self.query_circle(boundary, geometrical_center, radius, found_bodies)


    def __len__(self):
        """Return the number of points in the Node."""

        return self.bodies_number

    def draw(self, ax):
        """Draw a representation of the Node on Matplotlib Axes ax."""

        self.boundary.draw(ax)
        if not self.leaf:
            self.children['NE'].draw(ax)
            self.children['NW'].draw(ax)
            self.children['SE'].draw(ax)
            self.children['SW'].draw(ax)
    
    def _is_empty(self) :
        return self.bodies_number == 0


    def compute_acceleration(self, root):
        """
        Description: 
            Calculate acceleration for a given particle_id in the simulation with some tolerance theta
        Inputs:
            theta: opening angle (float)
            particle_id: index of particle in sim to calculate force for (int)
            G: gravitational constant (float)
        Output:
            grad: force array (1x3)
        """
        self.acceleration = self.traverse_compute(root)

        return self.acceleration
    
    def traverse_compute(self, root):
        """
        given two nodes n0 and n1, and some tol theta, traverse the tree till it's far enough that you can approximate the
        node as a "particle" and add the gravitational acceleration of that particle to the ret array. n1 is the leaf node that 
        holds the particle we are calculating the accel for.
        """
        if(self == root):
            return
        dr = root.center_of_mass - self.center_of_mass
        r = np.sqrt(np.sum(dr**2))
        size_of_node = root.boundary.h - self.boundary.h
        if(size_of_node/r < settings.THETA or root.leaf):
            self.body.acceleration += settings.GRAVITATION * root.mass * dr / (r**2 + settings.SOFTENING**2)**1.5
        
        elif self.body.position == root.body.position:
                    (self.body.velocity, root.body.velocity) = (root.body.velocity, self.body.velocity)
        else:
            for _ in root.children.keys:
                root.children[_].traverse_compute(root)
        return self.body.acceleration
