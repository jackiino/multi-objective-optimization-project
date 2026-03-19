import numpy as np
from config import lb, ub, mutation_strength, step_size
from evaluation import evaluation

def crossover(pop, n_offspring):
    offspring = np.zeros((n_offspring, pop.shape[1]))

    for i in range(n_offspring // 2):
        r1, r2 = np.random.choice(pop.shape[0], 2, replace=False)
        cp = np.random.randint(1, pop.shape[1])

        offspring[2*i, :cp] = pop[r1, :cp]
        offspring[2*i, cp:] = pop[r2, cp:]

        offspring[2*i+1, :cp] = pop[r2, :cp]
        offspring[2*i+1, cp:] = pop[r1, cp:]

    return offspring

def mutation(pop, n_offspring):
    offspring = np.zeros((n_offspring, pop.shape[1]))

    for i in range(n_offspring):
        idx = np.random.randint(pop.shape[0])
        child = pop[idx].copy()

        for j in range(pop.shape[1]):
            if np.random.rand() < 0.5:
                child[j] += np.random.uniform(-mutation_strength, mutation_strength)
                child[j] = np.clip(child[j], lb[j], ub[j])

        offspring[i] = child

    return offspring