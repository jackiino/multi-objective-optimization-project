import numpy as np
from config import lb, ub, step_size
from evaluation import evaluation

def local_search(pop, n_offspring):
    offspring = np.zeros((n_offspring, pop.shape[1]))

    for i in range(n_offspring):
        idx = np.random.randint(pop.shape[0])
        child = pop[idx].copy()

        j = np.random.randint(pop.shape[1])
        old_fit = evaluation(np.array([child]))[0]

        child[j] += np.random.uniform(-step_size, step_size)
        child[j] = np.clip(child[j], lb[j], ub[j])

        new_fit = evaluation(np.array([child]))[0]

        if new_fit[0] < old_fit[0] and new_fit[1] > old_fit[1]:
            offspring[i] = child
        else:
            offspring[i] = pop[idx]

    return offspring