from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.core.problem import Problem
from pymoo.optimize import minimize

from pkg.variable import Variable


class Solver:
    def __init__(self):
        self.problem = Problem(
            n_obj=1,
            n_ieq_constr=0,
            n_eq_constr=0,
            xu=None,
            vtype=Variable,
            vars=None,
            replace_nan_values_by=0
        )
        self.algorithm = NSGA2(pop_size=100)

    def solve(self):
        return minimize(
            self.problem,
            self.algorithm,
            ('n_gen', 200),
            seed=1,
            verbose=True
        )
