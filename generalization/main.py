from config import *
from population import random_population
from evaluation import evaluation
from selection import selection

from genetic_operations import crossover, mutation
from local_search import local_search

from plot import plot_pareto
from run_pymoo import run_pymoo

import numpy as np


def run_custom_nsga():
    pop = random_population(n_var, pop_size)

    for gen in range(max_gen):
        off_c = crossover(pop, rate_crossover)
        off_m = mutation(pop, mutation_rate)
        off_l = local_search(pop, rate_local_search)

        # Combine parents + offspring
        pop = np.vstack((pop, off_c, off_m, off_l))

        # Evaluate and select next generation
        fitness = evaluation(pop)
        pop = selection(pop, fitness, pop_size)

        print(f"Generation {gen}")

    return pop


if __name__ == "__main__":
    # --- Custom NSGA-II ---
    pop_custom = run_custom_nsga()
    plot_pareto(pop_custom, title="Custom NSGA-II Pareto Front")

    # --- Pymoo NSGA-II & NSGA-III ---
    res_nsga2, res_nsga3 = run_pymoo()

    # NSGA-II
    plot_pareto(res_nsga2.F, title="NSGA-II (pymoo) Pareto Front")

    # NSGA-III
    plot_pareto(res_nsga3.F, title="NSGA-III (pymoo) Pareto Front")

    # --- Print results ---
    print("Custom NSGA-II fitness values:\n", evaluation(pop_custom))
    print("Pymoo NSGA-II objectives:\n", res_nsga2.F)
    print("Pymoo NSGA-III objectives:\n", res_nsga3.F)