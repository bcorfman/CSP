from .util import PriorityQueue


def least_constrained(domains):
    return domains


def most_constrained(domains):
    return None


VAR_CHOICES = {'mcv': most_constrained,
               'lcv': least_constrained}

DOMAIN_CHOICES = {}


class Problem:
    def __init__(self, variables: list[str], domains: dict, constraints: list[str],
                 var_pick: str):
        self.variables = variables
        self.domains = PriorityQueue()
        for k, v in domains.items:
            self.domains.push((k, v), len(v))
        self.constraints = constraints
        self.var_pick = VAR_CHOICES[var_pick]

    def __repr__(self) -> str:
        return f'Problem({self.variables}, {self.domains}, {self.constraints})'

    def solve(self):
        assignment = set()
        remaining = set(self.variables)
        while True:
            if len(assignment) == len(self.variables):
                return assignment
            pick = self.var_pick(remaining)
            if not pick:
                remaining.append(assignment.pop())
                continue
