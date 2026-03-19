import matplotlib.pyplot as plt
from evaluation import evaluation
import numpy as np

def plot_pareto(pop, title="Pareto Front"):
    """
    Plot a single population or pymoo result in 3D.

    Parameters:
        pop : numpy array
            Population (solutions) OR fitness values
        title : str
            Plot title
    """
    # If this is a population, evaluate to get fitness
    if pop.ndim > 1 and pop.shape[1] > 3:
        fitness = evaluation(pop)
    else:
        fitness = pop  # already fitness values

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(fitness[:,0], fitness[:,1], fitness[:,2],
               c='blue', edgecolor='k', s=40, alpha=0.6)

    ax.set_xlabel('Objective 1')
    ax.set_ylabel('Objective 2')
    ax.set_zlabel('Objective 3')
    ax.set_title(title)

    plt.show()