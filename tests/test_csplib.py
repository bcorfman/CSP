from core.csplib import Problem, backtracking_search


def test_problem():
    # Australia map-coloring problem
    vars = ['wa', 'nt', 'sa', 'ql', 'nsw', 'v', 't']
    domains = {v: ['green', 'red', 'blue'] for v in vars}
    neighbors = {'sa': ['wa', 'nt', 'ql', 'nsw', 'v'], 'wa': ['nt', 'sa'],
                 'nt': ['ql', 'sa', 'wa'], 'ql': ['nt', 'nsw', 'sa'],
                 'nsw': ['v', 'ql', 'sa'], 'v': ['sa', 'nsw'], 't': []}
    constraints = ['sa != wa', 'sa != nt', 'sa != ql', 'sa != nsw', 'sa != v',
                   'wa != nt', 'nt != ql', 'ql != nsw', 'nsw != v']
    problem = Problem(vars, domains, neighbors, constraints)
    assert backtracking_search(problem) == {'wa': 'red', 'nt': 'green', 'sa': 'blue',
                                            'ql': 'red', 'nsw': 'green', 'v': 'red',
                                            't': 'green'}
