import matplotlib.pyplot as plt
import numpy as np

def plot_pareto(fitness_values, feasible_fitness_values):
    plt.scatter(fitness_values[:, 0], fitness_values[:, 1], label='Pareto optimal front')
    plt.scatter(np.array(feasible_fitness_values)[:, 0], np.array(feasible_fitness_values)[:, 1],
                label='Feasible solutions', color='orange')
    plt.legend(loc='best')
    plt.xlabel('Objective function F1')
    plt.ylabel('Objective function F2')
    plt.grid(True)
    plt.show()