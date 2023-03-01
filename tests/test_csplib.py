from core.csplib import Problem


def test_problem():
    # Australia map-coloring problem
    vars = ['wa', 'nt', 'sa', 'ql', 'nsw', 'v', 't']
    neighbors = {'sa': ['wa', 'nt', 'ql', 'nsw', 'v'], 'wa': ['nt', 'sa'],
                 'nt': ['ql', 'sa', 'wa'], 'ql': ['nt', 'nsw', 'sa'],
                 'nsw': ['v', 'ql', 'sa'], 'v': ['sa', 'nsw'], 't': []}
    domains = [['green', 'red', 'blue'] for _ in range(len(vars))]
    constraints = ['sa != wa', 'sa != nt', 'sa != ql', 'sa != nsw', 'sa != v',
                   'wa != nt', 'nt != ql', 'ql != nsw', 'nsw != v']
    problem = Problem(vars, domains, neighbors, constraints)
    assert problem.solve() == {'wa': 'red', 'nt': 'green', 'sa': 'blue',
                               'ql': 'red', 'nsw': 'green', 'v': 'red',
                               't': 'green'}
