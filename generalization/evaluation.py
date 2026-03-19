import numpy as np
from config import penalty_factor, negative_penalty_factor
from data import a, b, c, d

def evaluation(pop):
    fitness = np.zeros((pop.shape[0], 3))

    for i, x in enumerate(pop):
        f1 = -np.dot(a, x)
        f2 = np.dot(d, x)
        f3 = np.dot(b, x)

        g = np.dot(c, x) - 10000

        if g > 0:
            f2 += penalty_factor * g

        penalty = negative_penalty_factor * max(0, -np.min(x))

        fitness[i] = [f1 + penalty, f2 - penalty, f3 - penalty]

    return fitness