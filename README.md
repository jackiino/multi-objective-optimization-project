# NSGA-II main loop
start_time = time.time()  # Record the start time
for i in range(maximum_generation):
    offspring_from_crossover = crossover(pop, rate_crossover)
    offspring_from_mutation = mutation(pop, mutation_rate, mutation_strength)
    offspring_from_local_search = local_search(pop, rate_local_search, step_size)
    
    # we append childrens Q (cross-overs, mutations, local search) to paraents P
    # having parents in the mix, i.e. allowing for parents to progress to next iteration - Elitism
    pop = np.append(pop, offspring_from_crossover, axis=0)
    pop = np.append(pop, offspring_from_mutation, axis=0)
    pop = np.append(pop, offspring_from_local_search, axis=0)
    # print(pop.shape)
    fitness_values = evaluation(pop)
    pop = selection(pop, fitness_values, pop_size)  # we arbitrary set desired pereto front size = pop_size
    print('iteration:', i)

end_time = time.time()  # Record the end time
execution_time = end_time - start_time
print(f"Total execution time: {execution_time} seconds")



fitness_values = evaluation(pop)
index = np.arange(pop.shape[0]).astype(int)
pareto_front_index = pareto_front_finding(fitness_values, index)
pop = pop[pareto_front_index, :]
print("_________________")
print("Optimal solutions:")
print("x1  x2  x3")
for i in pareto_front_index:
    solution = pop[i]
    if is_feasible(solution):
        print(solution.astype(int))
print("solutions out of constraints:")
out_of_constraints_count = 0
for i in pareto_front_index:
    solution = pop[i]
    if not is_feasible(solution):
        out_of_constraints_count += 1
        print(solution.astype(int))
fitness_values = fitness_values[pareto_front_index]
print("______________")
print("Fitness values:")
print("  objective 1    objective 2")
print(fitness_values)

# Count how many solutions are out of constraints
out_of_constraints_count = sum([not is_feasible(pop[i]) for i in pareto_front_index])

print("Number of solutions out of constraints:", out_of_constraints_count)


fitness_values = evaluation(pop)
index = np.arange(pop.shape[0]).astype(int)
pareto_front_index = pareto_front_finding(fitness_values, index)

# Separate feasible and infeasible solutions
feasible_solutions = [pop[i] for i in pareto_front_index if is_feasible(pop[i])]
infeasible_solutions = [pop[i] for i in pareto_front_index if not is_feasible(pop[i])]

feasible_fitness_values = [fitness_values[i] for i in pareto_front_index if is_feasible(pop[i])]

