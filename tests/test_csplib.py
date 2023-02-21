from core.csplib import Problem


def test_problem():
    # Australia map-coloring problem
    vars = ['wa', 'nt', 'sa', 'ql', 'nsw', 'v', 't']
    domains = [['green', 'red', 'blue'] for _ in range(len(vars))]
    constraints = '''sa != wa and sa != nt and sa != ql and sa != nsw
                     sa != ql and sa != v and wa != nt and nt != ql and
                     ql != nsw and nsw != v'''
    problem = Problem(vars, domains, constraints)
    assert problem.solve() == {'wa': 'red', 'nt': 'green', 'sa': 'blue',
                               'ql': 'red', 'nsw': 'green', 'v': 'red',
                               't': 'green'}
