from src.utils import *

threshold = 100


def get_eigen(A, x):
    return (x.transpose() * A * x)[0][0]


def simple_iteration(A, x, eps=global_eps):
    A.square()

    count_iters = 0
    x = x.normalize()
    k = get_eigen(A, x)

    while (A * x - k * x).norm() >= eps:
        x = (A * x).normalize()
        k = get_eigen(A, x)
        count_iters += 1
        if count_iters > threshold:
            return 0
    return k, x