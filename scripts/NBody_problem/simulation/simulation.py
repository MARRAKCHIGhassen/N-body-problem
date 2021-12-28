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


# Functions
def launch_simulation():
    simulation_env = None
    settings.DIMENSION = 0

    if settings.DIMENSION == settings.PLAN : # Case Plan simulation (2D)
        # Creation of the space
        simulation_env = env.Plan()

        # Initialize Figure
        figure, axe_1, axe_2 = prepare_figure_2d_1()

    if settings.DIMENSION == settings.SPACE : # Case Space simulation (3D)
        # Creation of the space
        simulation_env = env.Space()
    
        # Initialize Figure
        figure, axe_1, axe_2, axe_3 = prepare_figure_3d()

    # Initialize time informations
    end_time = settings.END_TIME
    timestep = settings.TIMESTEP
    softening = settings.SOFTENING
    nbr_timesteps = int(np.ceil(end_time/timestep))

    # Simulation Main Loop
    for step in range(nbr_timesteps):
        # Update Informations
        simulation_env.update()

        # Plot
        if settings.DIMENSION == settings.PLAN : # Case Plan simulation (2D)
            # Creation of the space
            update_figure_2d_2(simulation_env, figure, axe_1, axe_2, step)


        if settings.DIMENSION == settings.SPACE : # Case Space simulation (3D)
            # Creation of the space
            update_figure_3d(simulation_env, figure, axe_1, axe_2, axe_3, step)
        
        plt.pause(0.001)

    # Show plot
    plt.show()

def update_figure_2d_2(simulation_space, figure, axe_1, axe_2, step):
    circle = [None]*settings.NUMBER_BODIES
    line  = [None]*settings.NUMBER_BODIES
    for i in range(settings.NUMBER_BODIES):
        circle[i] = plt.Circle((settings.Positions[i].x, settings.Positions[i].y), 0.08, ec="w", lw=2.5, zorder=20)
        axe_1.add_patch(circle[i])
        line[i] = axe_1.plot(settings.Positions[i].x[:0],settings.Positions[i].x[:0])[0]

def update_figure_2d(simulation_space, figure, axe_1, axe_2, step):
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

def update_figure_3d(simulation_space, figure, axe_1, axe_2, axe_3, step):
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

def prepare_figure_2d_1():
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(7, 7))
    ax1 = fig.add_subplot(1,1,1)
    plt.subplots_adjust(bottom=0.2,left=0.15)

    ax1.axis('equal')
    ax1.axis([-1, 30, -1, 30])
    ax1.xaxis.set_visible(False)
    ax1.yaxis.set_visible(False)
    return fig, ax1, ax1

def prepare_figure_2d():
    fig = plt.figure(figsize=(4,5), dpi=80)
    grid = plt.GridSpec(3, 1, wspace=0.0, hspace=0.3)
    ax1 = plt.subplot(grid[0:2,0])
    ax2 = plt.subplot(grid[2,0])

    return fig, ax1, ax2

def prepare_figure_3d():
    fig = plt.figure(figsize=(4,5), dpi=80)
    grid = plt.GridSpec(3, 1, wspace=0.0, hspace=0.3)
    ax1 = plt.subplot(grid[0:2,0])
    ax2 = plt.subplot(grid[2,0])
    ax3 = plt.subplot(grid[2,0])

    return fig, ax1, ax2, ax3