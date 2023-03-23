import random
from collections import Counter

from .util import PriorityQueue


class Problem:
    def __init__(self, variables: list[str], domains: dict, neighbors: dict,
                 constraints: list[str]):
        self.variables = variables
        self.domains = domains
        self.domain_queue = PriorityQueue()
        for k in neighbors.keys():
            num_vals = len(domains[k])
            self.domain_queue.push((k, domains[k]), num_vals)
        self.neighbors = neighbors
        self.constraints = constraints

    def __repr__(self) -> str:
        return f'''Problem({self.variables}, {self.domains}, {self.neighbors},
                {self.constraints})'''

    def goal(self, assignment) -> bool:
        return len(assignment) == len(self.variables)


# algorithms for selecting unassigned variables
def next_choice(assignment: dict, problem: Problem):
    return (set(problem.variables) - set(assignment.keys())).pop()


def random_choice(assignment: dict, problem: Problem):
    return random.choice(set(problem.variables) - set(assignment))


def minimum_remaining_values(assignment: dict, problem: Problem):
    remaining = set(problem.variables) - set(assignment)
    ctr = Counter()
    for var in remaining:
        new_assignment = dict(assignment)
        ctr[var] = len(problem.domains[var])
        for val in problem.domains[var]:
            new_assignment[var] = val
            for constraint in problem.constraints:
                if eval(constraint, new_assignment) is False:
                    ctr[var] -= 1
                    break
            del new_assignment[var]

    return ctr.most_common().pop()


# algorithms for ordering domain values
def no_ordering(var: str, assignment: dict, problem: Problem):
    return problem.domains[var]


# def least_constraining_value(var: str, assignment: dict, problem: Problem):
#     return problem.domains[var]


def consistent_with(assignment: dict, problem: Problem):
    return all(eval(constraint, assignment) for constraint in problem.constraints)


def backtracking_search(problem):
    def _recursive_backtracking(assignment: dict, problem: Problem, step_cost: int = 1,
                                select_unassigned_variable=minimum_remaining_values,
                                order_domain_values=no_ordering):
        if problem.goal(assignment):
            return assignment
        var = select_unassigned_variable(assignment, problem)
        cost = 0
        for val in order_domain_values(var, assignment, problem):
            new_assignment = dict(assignment).update({var: val})
            if consistent_with(new_assignment, problem.constraints):
                assignment[var] = val
                cost += 1
                result = _recursive_backtracking(assignment, problem, step_cost)
                if not result:
                    return result
                del assignment[var]
                cost -= 1
        return None

    return _recursive_backtracking({}, problem)
