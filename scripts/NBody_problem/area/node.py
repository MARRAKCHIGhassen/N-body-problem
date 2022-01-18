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
import NBody_problem.utils.log as log
import NBody_problem.geometry.vector as vector
import NBody_problem.geometry.boundary as bound
import NBody_problem.area.body as body

class Node:
    """A class implementing a Node."""

    def __init__(self, rectangle = bound.Rectangle(0, 0, 0), number_children=0):
        """Initialise le noeud à partir de sa géometrie.

        Parameters
        ----------
        rectangle : Rectangle
            La géométrie du noeud. Il définit la région à laquelle les corps appartiennent.
        """
        
        #------------------------------------------------ 

        log.log("STARTED", "node.py", "__init__")

        # Geometry
        self.boundary = rectangle
        self.children = {'NE' : None, 'SE' : None, 'NW' : None, 'SW' : None}
        self.number_children = number_children

        # Bodies
        self.bodies_number = 0
        self.total_mass = 0.0
        self.bodies = []
        self.center_of_mass = vector.Vector(0, 0, 0)
        self.body = 0

        # Leaf Indicator
        self.leaf = False

        log.log("ENDED", "node.py", "__init__")

    def insert(self, body):
        """Try to insert Point point into this Node."""

        # Si le corps n'appartient pas au noeud.
        if not self.boundary.contains(body.position): 
            return False
        
        # Si le noeud ne contient pas de corps
        if self.bodies_number < settings.Max_bodies:
            self.bodies_number += 1
            self.total_mass += body.mass
            self.center_of_mass = body.position
            self.body = body.id
            self.bodies.append(body.id)
            self.leaf = True

            settings.N_Body_Nodes[body.id] = self

            return True

        # Si noeud interne déjà subdivisé
        if(not self.leaf):
            # Mettre à jour le centre de masse
            self.bodies.append(body.id)
            self.total_mass += body.mass
            self.bodies_number += 1

            # Mettre à jour le centre de masse
            self.update_com()

            for _ in self.children.keys():
                if(self.children[_].boundary.contains(body.position)) :
                    self.children[_].insert(body)
                    return True
            
        else: # Si noeud contient un corps et il doit être subdivisé
            # Mettre à jour le centre de masse
            self.bodies.append(body.id)
            self.total_mass += body.mass
            self.bodies_number += 1

            self.divide()
            self.update_com()

            for _ in self.children.keys():
                if(self.children[_].boundary.contains(body.position)) :
                    self.children[_].insert(body)
                    return True
    
        return False

    def update_com(self):
        """
        updates center of mass. p self-explanatory
        """
        self.center_of_mass = vector.Vector(0, 0, 0)
        for body_index in self.bodies :
            self.center_of_mass.x = settings.N_bodies[body_index].position.x * settings.N_bodies[body_index].mass / self.total_mass
            self.center_of_mass.y = settings.N_bodies[body_index].position.y * settings.N_bodies[body_index].mass / self.total_mass
            self.center_of_mass.z = settings.N_bodies[body_index].position.z * settings.N_bodies[body_index].mass / self.total_mass
        
        return

    def divide(self):
        """Subdivise le noeud en 4 sous-noeuds."""

        # Informations utiles à la subdivision
        center_x, center_y = self.boundary.center_x, self.boundary.center_y
        arete_child = self.boundary.arete / 2

        # Création des fils (géométriquement)
        self.children['SW'] = Node(bound.Rectangle(center_x - arete_child/2, center_y - arete_child/2, arete_child),
                                    self.number_children + 1)
        self.children['SE'] = Node(bound.Rectangle(center_x + arete_child/2, center_y - arete_child/2, arete_child),
                                    self.number_children + 1)
        self.children['NE'] = Node(bound.Rectangle(center_x + arete_child/2, center_y + arete_child/2, arete_child),
                                    self.number_children + 1)
        self.children['NW'] = Node(bound.Rectangle(center_x - arete_child/2, center_y + arete_child/2, arete_child),
                                    self.number_children + 1)
        # Rendre noeud interne
        self.leaf = False 

    def traverse_compute(self, root):
        """A partir de la racine, le noeud appelant traverse l'arbre jusqu'à atteindre un noeud suffisement loin pour approximer en un seul corps. L'appel est récursif sur tout les enfants de chaque noeud.
        
        Parameters
        ----------
        root : Node
            La racine de l'arbre quadratique.

        Returns
        -------
        acceleration : float
            La nouvelle valeur d'accelération.
        """

        #------------------------------------------------

        log.log("STARTED", "body.py", "traverse_compute")

        if(self == root): # Ne rien faire s'il s'agit du noeud racine
            return
        
        # Les critères d'évaluation
        d = vector.Vector.distance(self.center_of_mass, root.center_of_mass)
        s = root.boundary.arete

        # Vérification
        if((s/d < settings.Theta) or root.leaf): 
            settings.N_bodies[self.body].acceleration += settings.Gravitation * root.total_mass * (self.center_of_mass - root.center_of_mass).abs() / (d**2 + settings.Softening**2)**1.5
        else:
            for _ in root.children.keys(): # itérer tout les enfant
                if root.children[_] != None :
                    self.traverse_compute(root.children[_])

        return settings.N_bodies[self.body].acceleration

    def __str__(self):
        """Retourne le noeud sous forme de chaine de caractère formattée

        Returns
        -------
        string : str
            La chaine formattée
        """

        #------------------------------------------------

        space = ' ' * self.number_children * 2
        string = str(self.boundary) + '\n'
        string += space + ', '.join(str(settings.N_bodies[body]) for body in self.bodies)

        if self.leaf:
            return string
        
        return string + '\n' + '\n'.join([
                space + 'nw: ' + str(self.children['NW']), space + 'ne: ' + str(self.children['NE']),
                space + 'se: ' + str(self.children['SW']), space + 'sw: ' + str(self.children['SW'])])









"""
    def query(self, boundary, found_bodies):
        Find the points in the Node that lie within boundary.

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
        Find the points in the Node that lie within radius of centre.

        boundary is a Rect object (a square) that bounds the search circle.
        There is no need to call this method directly: use query_radius.

        

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
        Find the points in the Node that lie within radius of centre

        # First find the square that bounds the search circle as a Rect object.
        boundary = bound.Rectangle(*geometrical_center, 2*radius, 2*radius)
        return self.query_circle(boundary, geometrical_center, radius, found_bodies)

    def draw(self, ax):
        Draw a representation of the Node on Matplotlib Axes ax.

        self.boundary.draw(ax)
        if not self.leaf:
            self.children['NE'].draw(ax)
            self.children['NW'].draw(ax)
            self.children['SE'].draw(ax)
            self.children['SW'].draw(ax)
    

            print("root.center_of_mass", root.center_of_mass)
            print("self.center_of_mass", self.center_of_mass)
            print("self.center_of_mass - root.center_of_mass", self.center_of_mass - root.center_of_mass)
            print("(self.center_of_mass - root.center_of_mass).abs()", (self.center_of_mass - root.center_of_mass).abs())
            print("root.total_mass * (self.center_of_mass - root.center_of_mass).abs()", root.total_mass * (self.center_of_mass - root.center_of_mass).abs())
            print("d", d)
            print("d**2", d**2)
            print("settings.Softening", settings.Softening)
            print(" (d**2 + settings.Softening**2)**1.5",  (d**2 + settings.Softening**2)**1.5)
            acc_1 = settings.Gravitation * root.total_mass * (self.center_of_mass - root.center_of_mass).abs() / (d**2 + settings.Softening**2)**1.5
            acc_2 = settings.N_bodies[self.body].acceleration
            print("acc_1", acc_1)
            print("acc_2", acc_2)
            settings.N_bodies[self.body].acceleration.x += settings.Gravitation * root.total_mass * (self.center_of_mass - root.center_of_mass).abs() / (d**2 + settings.Softening**2)**1.5
            settings.N_bodies[self.body].acceleration.y += settings.Gravitation * root.total_mass * (self.center_of_mass - root.center_of_mass).abs() / (d**2 + settings.Softening**2)**1.5
"""
