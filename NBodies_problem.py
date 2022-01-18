# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from random import uniform
from numba import jit, cuda

import NBody_problem.settings as settings
import NBody_problem.bodies as bodies
import NBody_problem.geometry as geo

def generate_bodies():
    # instantiate bodies with mass
    for body_index in range(settings.Number_bodies) :
        body = bodies.Body()
        body.id = body_index
        body.mass = uniform(1, 20)

        # append to list
        settings.N_bodies.append(body)

    # Positions & Velocités
    for body_index in range(settings.Number_bodies) :
        position = geo.Vector(uniform(-settings.Arete/2*0.8, settings.Arete/2*0.8), uniform(-settings.Arete/2*0.8, settings.Arete/2*0.8))
        velocity = geo.Vector(0, 0)
        
        settings.N_bodies[body_index].position = position
        settings.Positions.append(position)

        settings.N_bodies[body_index].velocity = velocity

if __name__ == '__main__' :
    # Génération des corps
    generate_bodies()

    # Instanciation de l'environnement (avec la structure de quadtree)
    simulation_env = bodies.Plan()

    # Calcul des accélérations initiales
    for body_index in range(settings.Number_bodies) :
        simulation_env.compute_acceleration(simulation_env.root, body_index)
    
    # Positions Au fil du temps
    xx = [pos.x for pos in settings.Positions]
    yy = [pos.y for pos in settings.Positions]

    # Initialisation de la figure
    fig = plt.figure(dpi=80)
    fig.canvas.set_window_title('N-Body Problem')

    # Premier plot
    plt.scatter(xx, yy, s=3, color=[.7,.7,1])
    
    # Initialisation des pas
    nbr_timesteps = int(np.ceil(settings.End_time/settings.Timestep))

    # La boucle principale de la simulation
    for step in range(nbr_timesteps):
        plt.cla()
        plt.xlim(-settings.Arete/2, settings.Arete/2)
        plt.ylim(-settings.Arete/2, settings.Arete/2)

        # Quitter en cas de 0 corps existant (dans le cas de gestion de collision par absorption)
        if len(xx) == 0 or len(yy) == 0 :
            plt.close(fig)
            break
        
        # plot
        plt.scatter(xx, yy, s=5, color='blue')
        #plt.scatter(xx, yy, s=1, color=[.7,.7,1])
        

        # Update Informations
        # Environnement
        simulation_env.update()

        # Coordonnées
        xx = [pos.x for pos in settings.Positions]
        yy = [pos.y for pos in settings.Positions]

        plt.pause(0.01)
    
    # Show plot
    plt.show(block=False)
