import numpy as np
from pymoo.core.problem import ElementwiseProblem
from config import n_var, lb, ub
from data import a, b, c, d

class MyProblem(ElementwiseProblem):

    def __init__(self):
        super().__init__(n_var=n_var, n_obj=3, n_ieq_constr=1, xl=lb, xu=ub)

    def _evaluate(self, x, out, *args, **kwargs):
        f1 = -np.dot(a, x)
        f2 = np.dot(d, x)
        f3 = np.dot(b, x)
        g1 = np.dot(c, x) - 10000

        out["F"] = [f1, f2, f3]
        out["G"] = [g1]