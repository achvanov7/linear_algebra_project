global_eps = 1e-9


def eq(a, b, eps=global_eps):
    return abs(a - b) < eps
