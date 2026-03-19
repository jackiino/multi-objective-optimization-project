from pymoo.optimize import minimize
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.algorithms.moo.nsga3 import NSGA3
from pymoo.util.ref_dirs import get_reference_directions

from problem import MyProblem

def run_pymoo():
    problem = MyProblem()

    res2 = minimize(problem, NSGA2(pop_size=600), ('n_gen', 150))

    ref_dirs = get_reference_directions("das-dennis", 3, n_partitions=33)
    res3 = minimize(problem, NSGA3(pop_size=600, ref_dirs=ref_dirs), ('n_gen', 300))

    return res2, res3