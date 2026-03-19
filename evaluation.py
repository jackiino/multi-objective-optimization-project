import numpy as np
from config import penalty_factor, negative_penalty_factor

def evaluation(pop):
    fitness_values = np.zeros((pop.shape[0], 2))  # Two objectives

    for i, x in enumerate(pop):
        obj1 = -10 * x[0] - 6 * x[1] - 4 * x[2]
        obj2 = 7 * x[0] + 4 * x[1] + 3 * x[2]

        constraint1 = 4 * x[0] + 3 * x[1] + 2 * x[2] - 1300
        constraint2 = 3 * x[0] + 3 * x[1] + 1 * x[2] - 1000

        # Penalty for negativity of at least one variable
        negativity_penalty = negative_penalty_factor * max(0, -min(x))

        if constraint1 > 0:
            obj1 += penalty_factor * constraint1
        if constraint2 > 0:
            obj2 -= penalty_factor * constraint2

        # Combine objectives with penalty for negativity
        fitness_values[i, 0] = obj1 + negativity_penalty
        fitness_values[i, 1] = obj2 - negativity_penalty

    return fitness_values