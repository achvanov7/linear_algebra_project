from src.utils import *

threshold = 20


def check_gershgorin_circles(A):
    circles = A.gershgorin_circles()
    max_dist = 0
    for cent, rad in circles:
        max_dist = max(max_dist, abs(cent) + rad)
    return max_dist > 1


def simple_iteration_method(A, b, eps=global_eps):
    x = Matrix.random(A.width, 1)

    count_fail_iters = 0
    big_circles = check_gershgorin_circles(A)

    while (x - A * x - b).norm() >= eps:
        x_new = A * x + b

        if abs(x.norm() - x_new.norm()) >= 1:
            count_fail_iters += 1
        else:
            count_fail_iters = 0

        x = x_new
        if count_fail_iters > threshold and big_circles:
            return 0

    return x
