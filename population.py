import numpy as np

def random_population(n_var, n_sol, lb, ub):
    # n_var = number of variables
    # n_sol = number of random solutions
    # lb = lower bound for variable values
    # ub = upper bound for variable values
    
    # Initialize an array to store the population
    pop = np.zeros((n_sol, n_var))
    
    # Generate random solutions for each variable in each solution
    for i in range(n_sol):
        # For each solution, generate random values for each variable within the specified bounds
        pop[i, :] = np.random.uniform(lb, ub)
    
    # Return the generated random population
    return pop