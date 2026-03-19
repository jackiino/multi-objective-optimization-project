import numpy as np
from config import lb, ub

def random_population(n_var, n_sol):
    return np.random.uniform(lb, ub, (n_sol, n_var))