import numpy as np
from config import lb, ub
from evaluation import evaluation

def local_search(pop, n_sol, step_size):
    offspring = np.zeros((n_sol, pop.shape[1]))
    for i in range(n_sol):
        r1 = np.random.randint(0, pop.shape[0]) 
        individual = pop[r1, :].copy()  # Copy the selected individual
        r2 = np.random.randint(0, pop.shape[1])
        original_fitness = evaluation(np.array([individual]))[0]

        # Perform local search
        individual[r2] += np.random.uniform(-step_size, step_size)
        
        if individual[r2] < lb[r2]:
            individual[r2] = lb[r2]
        if individual[r2] > ub[r2]:
            individual[r2] = ub[r2]

        new_fitness = evaluation(np.array([individual]))[0]

        # Check if the new individual has better fitness
        if new_fitness[0] < original_fitness[0] and new_fitness[1] > original_fitness[1]:
            offspring[i, :] = individual
        else:
            offspring[i, :] = pop[r1, :]  # Keep the original individual

    return offspring