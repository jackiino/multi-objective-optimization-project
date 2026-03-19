import numpy as np
from config import lb, ub

def crossover(pop, crossover_rate):
    offspring = np.zeros((crossover_rate, pop.shape[1])) # pop.shape returns a tuple representing the dimension of the array pop, pop.shape[1] extracts the second element, which corresponds to the number of columns or variables in the array
    for i in range(int(crossover_rate/2)): # we perform crossover only for a half of the population in order to have a balance between exploration and exploitation
        r1 = np.random.randint(0, pop.shape[0])
        r2 = np.random.randint(0, pop.shape[0])

    # in order to be sure that the selected parents are distinct
        while r1 == r2:
            r1 = np.random.randint(0, pop.shape[0])
            r2 = np.random.randint(0, pop.shape[0])

        # select a random cutting point for crossover
        cutting_point = np.random.randint(1, pop.shape[1])

        # Perform crossover
        offspring[2*i, 0:cutting_point] = pop[r1, 0:cutting_point] #at each iteration two offsprings are created
        offspring[2*i, cutting_point:] = pop[r2, cutting_point:]
        offspring[2*i+1, 0:cutting_point] = pop[r2, 0:cutting_point]
        offspring[2*i+1, cutting_point:] = pop[r1, cutting_point:]
        
    return offspring



def mutation(pop, mutation_rate, mutation_strength):
    offspring = np.zeros((mutation_rate, pop.shape[1]))

    for i in range(mutation_rate):
        parent_index = np.random.randint(0, pop.shape[0])
        mutated_individual = pop[parent_index].copy()

        for gene_index in range(pop.shape[1]):
            if np.random.rand() < 0.5:  # 50% chance to mutate this gene
                mutation_value = np.random.uniform(-mutation_strength, mutation_strength)
                mutated_individual[gene_index] += mutation_value

                # Ensure the mutated value stays within bounds
                mutated_individual[gene_index] = max(lb[gene_index], min(ub[gene_index], mutated_individual[gene_index]))

        offspring[i] = mutated_individual

    return offspring
