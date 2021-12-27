# -*- coding: utf-8 -*-
"""Simulation Module

Simulating the problem

Name
-------
simulation

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
import numpy as np
import matplotlib.pyplot as plt

# Import custom libraries
import NBody_problem.area.environment as env
import NBody_problem.utils.config as config
import NBody_problem.utils.settings as settings


# Global variable
Dimension = 0


# Functions
def launch_simulation(NBodies):
    simulation_env = None
    Dimension = config.get_environment_dimension()

    if Dimension == settings.PLAN : # Case Plan simulation (2D)
        # Creation of the space
        simulation_env = env.Plan(NBodies)


    if Dimension == settings.SPACE : # Case Space simulation (3D)
        # Creation of the space
        simulation_env = env.Space(NBodies)
    
    # Initialize Figure
    figure, axe_1, axe_2 = prepare_figure()

    # Initialize time informations
    end_time = config.get_simulation_duration()
    timestep = config.get_simulation_timestep()
    softening = config.get_simulation_softening()
    nbr_timesteps = int(np.ceil(end_time/timestep))

    # Simulation Main Loop
    for step in range(nbr_timesteps):
        # Update Informations
        simulation_env.update(softening)

        # Plot
        update_figure(simulation_env, figure, axe_1, axe_2, step)

        plt.pause(0.001)

def update_figure(simulation_space, figure, axe_1, axe_2, step):
    plt.sca(axe_1)
    plt.cla()
    xx = position[:,0,max(index-50,0):index+1]
    yy = position[:,1,max(index-50,0):index+1]
    plt.scatter(xx,yy,s=1,color=[.7,.7,1])
    plt.scatter(drift[:,0],drift[:,1],s=10,color='blue')
    axe_1.set(xlim=(-2, 2), ylim=(-2, 2))
    axe_1.set_aspect('equal', 'box')
    axe_1.set_xticks([-2,-1,0,1,2])
    axe_1.set_yticks([-2,-1,0,1,2])
    
    plt.sca(axe_2)
    plt.cla()
    plt.scatter(t_all,KE_save,color='red',s=1,label='KE' if index == Nt-1 else "")
    plt.scatter(t_all,PE_save,color='blue',s=1,label='PE' if index == Nt-1 else "")
    plt.scatter(t_all,KE_save+PE_save,color='black',s=1,label='Etot' if index == Nt-1 else "")
    axe_2.set(xlim=(0, tEnd), ylim=(-300, 300))
    axe_2.set_aspect(0.007)

def prepare_figure():
    fig = plt.figure(figsize=(4,5), dpi=80)
    grid = plt.GridSpec(3, 1, wspace=0.0, hspace=0.3)
    ax1 = plt.subplot(grid[0:2,0])
    ax2 = plt.subplot(grid[2,0])

    return fig, ax1, ax2

