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

# Import custom libraries
import NBody_problem.utils.settings as settings
import NBody_problem.utils.log as log

import NBody_problem.area.node as node
import NBody_problem.geometry.vector as vector
import NBody_problem.geometry.boundary as bound


class Plan:
    def __init__(self):
        """Constructeur de l'environnement de simulation (contenant les points)."""
	
        #------------------------------------------------ 

        log.log("STARTED", "environment.py", "__init__")
        
        self.construct()

        log.log("ENDED", "environment.py", "__init__")

    def construct(self):
        """batit l'arbre."""
	
        #------------------------------------------------ 

        log.log("STARTED", "environment.py", "construct")

        # Geometry
        arete = settings.Arete
        rectangle = bound.Rectangle(0, 0, arete)
        
        # Construct
        self.root = node.Node(rectangle = rectangle)

        # Bodies
        for body_index in range(settings.Number_bodies) :
            self.root.insert(settings.N_bodies[body_index])

        log.log("ENDED", "environment.py", "construct")

    def update(self):
        """Met à jour l'envrionnement après écoulement de temps (1 timestep)."""
	
        #------------------------------------------------ 

        log.log("STARTED", "environment.py", "update")

        # Calcul des accelérations
        for body_index in range(settings.Number_bodies) :
            self.compute_acceleration(self.root, body_index)
        
        # Calcul des autres paramètres
        for body_index in range(settings.Number_bodies) :
            settings.N_bodies[body_index].compute_remain_parameters()
        
        # Reconstruction de l'arbre
        self.construct()

        log.log("ENDED", "environment.py", "update")


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
        
        log.log("STARTED", "environment.py", "compute_acceleration")

        # Trouver le noeud correspondant
        node = settings.N_Body_Nodes[body_index]

        # Appel de méthode récurisve
        node.traverse_compute(root)

        log.log("ENDED", "environment.py", "compute_acceleration")









"""
    def insert_bodies(self, root):
        Insère les corps à partir de la liste de settings.
        
        Parameters
        ----------
        root : Node
            La racine de l'arbre que va construire la fonction.
        
        
        #------------------------------------------------ 
        
        log.log("STARTED", "environment.py", "insert_bodies")

        # Noeud intermédiaire
        node_inter = 


        log.log("ENDED", "environment.py", "insert_bodies")

class Space:
    def __init__(self, NBodies):
        # Theta
        self._theta = config.get_space_theta()
        
        # Gravitation
        self._gravitation = config.get_space_gravitation()
        
        # Root
        arete = config.get_space_arete()
        geometrical_center = vector.Vector(0, 0, 0)
        self.root = node.Node(geometrical_center = geometrical_center, arete = arete)
        self.root.insert(NBodies)

    
    def get_theta(self):
        return self._theta


    def get_gravitation(self):
        return self._gravitation
    

    def _construct_space(self, NBodies):
        # Fetch the bodies informations
        arete = config.get_space_arete()
        
        # Root construction
        self.root = node.Node(geometrical_center = vector.Vector(0, 0, 0), 
                              arete = arete, 
                              bodies_number = bodies_number, 
                              bodies_positions = bodies_positions, 
                              bodies_masses = bodies_masses)

        return self.root
    
    def generate_initial_conditions(NBodies):
        np.random.seed(17)            # set the random number generator seed
        mass = 20.0*np.ones((self.root.get_bodies_number(),1))/self.root.get_bodies_number()  # total mass of particles is 20
        pos  = np.random.randn(N,3)   # randomly selected positions and velocities
        vel  = np.random.randn(N,3)

        print('test')

    """