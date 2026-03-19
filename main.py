import time
from config import *
from population import random_population
from genetic_operations import crossover, mutation
from local_search import local_search
from evaluation import evaluation
from selection import selection, is_feasible, pareto_front_finding
from plot import plot_pareto
import numpy as np

pop = random_population(n_var, pop_size, lb, ub)

start_time = time.time()
for i in range(maximum_generation):
    offspring_c = crossover(pop, rate_crossover)
    offspring_m = mutation(pop, mutation_rate, mutation_strength)
    offspring_ls = local_search(pop, rate_local_search, step_size)

    pop = np.append(pop, offspring_c, axis=0)
    pop = np.append(pop, offspring_m, axis=0)
    pop = np.append(pop, offspring_ls, axis=0)

    fitness_values = evaluation(pop)
    pop = selection(pop, fitness_values, pop_size)
    print("Iteration:", i)

end_time = time.time()
print("Execution time:", end_time - start_time)

# Separate feasible solutions
fitness_values = evaluation(pop)
pareto_index = np.arange(pop.shape[0]).astype(int)
pareto_front_index = pareto_front_finding(fitness_values, pareto_index)

feasible_solutions = [pop[i] for i in pareto_front_index if is_feasible(pop[i])]
feasible_fitness_values = [fitness_values[i] for i in pareto_front_index if is_feasible(pop[i])]

plot_pareto(fitness_values, feasible_fitness_values)