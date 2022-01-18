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
import NBody_problem.utils.settings as settings
import NBody_problem.utils.log as log


# Functions
def launch_simulation():
    """Instructions principales de la simulation."""
	
	#------------------------------------------------ 

    log.log("STARTED", "simulation.py", "launch_simulation")

    simulation_env = env.Plan()

    # Initialize Figure
    #figure, axe = prepare_figure()
    plt.figure(figsize=(4,5), dpi=80)

    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    #plt.aspect('equal', 'box')
    plt.xticks([-2,-1,0,1,2])
    plt.yticks([-2,-1,0,1,2])

    # Initialize number of steps
    nbr_timesteps = int(np.ceil(settings.End_time/settings.Timestep))

    # Simulation Main Loop
    for step in range(nbr_timesteps):
        # Update Informations
        simulation_env.update()

        # Plot
        #update_figure(axe)
        xx = [pos.x for pos in settings.Positions]
        print("len xx : ", xx)
        yy = [pos.y for pos in settings.Positions]
        print("len yy : ", yy)
        for _ in settings.N_Body_Nodes.keys():
            print(_ , ' ||| ', settings.N_Body_Nodes[_])
        print(str(simulation_env.root))
        print(str(simulation_env.root))
        input("test")
        plt.scatter(xx,yy, s=1, color=[.7,.7,1])

        plt.pause(0.1)

    # Show plot
    plt.show()

    log.log("ENDED", "simulation.py", "launch_simulation")


def prepare_figure() :
    """Préparer la figure

    Returns
    -------
    fig : figure
        La figure de plot.
    
    axe : axe
        L'axe du plot.
    """

    #------------------------------------------------

    log.log("STARTED", "simulation.py", "prepare_figure")

    fig, axe = plt.figure(figsize=(4,5), dpi=80)

    axe.set(xlim=(-2, 2), ylim=(-2, 2))
    axe.set_aspect('equal', 'box')
    axe.set_xticks([-2,-1,0,1,2])
    axe.set_yticks([-2,-1,0,1,2])

    return fig, axe


def update_figure(axe):
    """Mise à jour de la figure

    Parameters
    ----------
    axe : plot axe
        L'axe de la figure.
    """

    #------------------------------------------------

    log.log("STARTED", "simulation.py", "update_figure")

    plt.sca(axe)

    # Get les coordonnées
    xx = [pos.x for pos in settings.Positions]
    yy = [pos.y for pos in settings.Positions]

    plt.scatter(xx,yy, s=1, color=[.7,.7,1])

    log.log("ENDED", "simulation.py", "update_figure")
