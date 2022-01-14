# -*- coding: utf-8 -*-
# Importing Global Libraries
import math

# Import custom libraries
import NBody_problem.settings as settings
import NBody_problem.geometry as geo


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

        self.id = id
        self.mass = mass
        self.position = geo.Vector(0, 0, 0)
        self.velocity = geo.Vector(0, 0, 0)
        self.acceleration = geo.Vector(0, 0, 0)

    def compute_remain_parameters(self) :
        """Calcule, après le calcul de l'accélération, la position et la vélocité."""

        #------------------------------------------------

        # Positions
        self.position += self.velocity + self.acceleration * 0.5
        settings.Positions[self.id] = self.position

        # Velocities
        self.velocity += self.acceleration

    def __str__(self):
        """convert the body to string.

        Returns
        -------
        str : str
            Body converted & formatted to a string.
        """

        #------------------------------------------------
        
        body_str = '\n'
        body_str += '([body_{id}]\n)'.format(id=self.id)
        body_str += '(mass         : {mass}\n)'.format(mass=self.mass)
        body_str += '(position     : {position}\n)'.format(position=self.position)
        body_str += '(velocity     : {velocity}\n)'.format(velocity=self.velocity)
        body_str += '(acceleration : {acceleration}\n)'.format(acceleration=self.acceleration)
        body_str += '---\n'

        return body_str


## NODE
class Node:
    """A class implementing a Node."""

    def __init__(self, rectangle = geo.Rectangle(0, 0, 0), number_children=0):
        """Initialise le noeud à partir de sa géometrie.

        Parameters
        ----------
        rectangle : Rectangle
            La géométrie du noeud. Il définit la région à laquelle les corps appartiennent.
        """
        
        #------------------------------------------------ 

        # Geometry
        self.boundary = rectangle
        self.children = {'NE' : None, 'SE' : None, 'NW' : None, 'SW' : None}
        self.number_children = number_children

        # Bodies
        self.bodies_number = 0
        self.total_mass = 0.0
        self.bodies = []
        self.center_of_mass = geo.Vector(0, 0, 0)
        self.body = 0

        # Leaf Indicator
        self.leaf = False

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
        self.center_of_mass = geo.Vector(0, 0, 0)
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
        self.children['SW'] = Node(geo.Rectangle(center_x - arete_child/2, center_y - arete_child/2, arete_child),
                                    self.number_children + 1)
        self.children['SE'] = Node(geo.Rectangle(center_x + arete_child/2, center_y - arete_child/2, arete_child),
                                    self.number_children + 1)
        self.children['NE'] = Node(geo.Rectangle(center_x + arete_child/2, center_y + arete_child/2, arete_child),
                                    self.number_children + 1)
        self.children['NW'] = Node(geo.Rectangle(center_x - arete_child/2, center_y + arete_child/2, arete_child),
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

        if(self == root): # Ne rien faire s'il s'agit du noeud racine
            return
        
        # Les critères d'évaluation
        
        d = geo.Vector.distance(self.center_of_mass, root.center_of_mass)
        s = root.boundary.arete
        """
        f = settings.Gravitation * root.total_mass * settings.N_bodies[self.body]
        dx = root.center_of_mass.x - self.center_of_mass.x
        dy = root.center_of_mass.y - self.center_of_mass.y
        dz = root.center_of_mass.y - self.center_of_mass.y
        angle = math.atan2(dy, dx)
        fx = math.cos(angle) * f
        fy = math.sin(angle) * f
        """

        # Vérification
        if((s/d < settings.Theta) or root.leaf): 
            temp = settings.Gravitation * root.total_mass / math.pow((self.center_of_mass - root.center_of_mass).abs(), 3)
            settings.N_bodies[self.body].acceleration += (root.center_of_mass - self.center_of_mass) * temp
            #settings.N_bodies[self.body].acceleration += settings.Gravitation * root.total_mass * (self.center_of_mass - root.center_of_mass).abs() / (d**2 + settings.Softening**2)**1.5
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


## PLAN
class Plan:
    def __init__(self):
        """Constructeur de l'environnement de simulation (contenant les points)."""
	
        #------------------------------------------------ 
        
        self.construct()

    def construct(self):
        """batit l'arbre."""
	
        #------------------------------------------------ 

        # Geometry
        arete = settings.Arete
        rectangle = geo.Rectangle(0, 0, arete)
        
        # Construct
        self.root = Node(rectangle = rectangle)

        # Bodies
        for body_index in range(settings.Number_bodies) :
            self.root.insert(settings.N_bodies[body_index])

    def update(self):
        """Met à jour l'envrionnement après écoulement de temps (1 timestep)."""
	
        #------------------------------------------------ 

        # Calcul des accelérations
        for body_index in range(settings.Number_bodies) :
            self.compute_acceleration(self.root, body_index)
        
        # Calcul des autres paramètres
        for body_index in range(settings.Number_bodies) :
            settings.N_bodies[body_index].compute_remain_parameters()
        
        # Reconstruction de l'arbre
        self.construct()


    def compute_acceleration(self, root, body_index):
        """Calcule l'accélération du noeud d'indice "body_index".
        
        Parameters
        ----------
        root : Node
            La racine de l'arbre à partir de laquelle la fonction commence l'exploration (peut être la rcine de l'arbre ou un noeud).
        
        body_index : int
            L'indice du corps que la fonction lui calcule l'accelération.
        """
        
        #------------------------------------------------ 

        # Trouver le noeud correspondant
        node = settings.N_Body_Nodes[body_index]

        # Appel de méthode récurisve
        node.traverse_compute(root)

