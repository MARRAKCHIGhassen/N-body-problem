# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

import NBody_problem.settings as settings
import NBody_problem.bodies as bodies
import NBody_problem.geometry as geo

def generate_bodies():
    # instantiate bodies with mass
    for body_index in range(settings.Number_bodies) :
        body = bodies.Body()
        body.id = body_index
        body.mass = 20.0

        # append to list
        settings.N_bodies.append(body)

    
    # Random
    np.random.seed(17)            # set the random number generator seed
    pos  = np.random.randn(settings.Number_bodies,3)   # randomly selected positions and velocities
    vel  = np.random.randn(settings.Number_bodies,3)
    
    # Bodies
    for body_index in range(settings.Number_bodies) :
        # Informations
        position = geo.Vector(pos[body_index, 0], pos[body_index, 1], pos[body_index, 2])
        velocity = geo.Vector(vel[body_index, 0], vel[body_index, 1], vel[body_index, 2])
        acceleration = geo.Vector(0, 0, 0)

        settings.N_bodies[body_index].position = position
        settings.Positions.append(position)

        settings.N_bodies[body_index].velocity = velocity
        settings.N_bodies[body_index].acceleration = acceleration

if __name__ == '__main__' :
    # Generate bodies
    generate_bodies()

    # Initialize environment
    simulation_env = bodies.Plan()

    # Initialize Figure
    plt.figure(figsize=(4,5), dpi=80)
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.xticks([-2,-1,0,1,2])
    plt.yticks([-2,-1,0,1,2])

    # Initialize number of steps
    nbr_timesteps = int(np.ceil(settings.End_time/settings.Timestep))

    # Simulation Main Loop
    for step in range(nbr_timesteps):
        # Update Informations
        simulation_env.update()

        # Plot
        # Coordinates
        xx = [pos.x for pos in settings.Positions]
        yy = [pos.y for pos in settings.Positions]

        plt.scatter(xx, yy, s=1, color=[.7,.7,1])
        #plt.scatter(xx, yy, s=10, color='blue')

        plt.pause(0.01)

    # Show plot
    plt.show()