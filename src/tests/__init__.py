from src.utils import *
from src.simple_iteration import *
from src.gauss_zeidel import *
import random

eps = 1e-14


def simple_iteration_test(A, b):
    x = simple_iteration_method(A, b, eps)
    assert (x == A * x + b)
    print("Simple Iteration: OK")


def gauss_zeidel_test(A, b):
    x = gauss_zeidel(A, b, eps)
    assert (A * x == b)
    print("Gauss-Zeidel test: OK")


def run_all_tests():
    A = Matrix([
        [0.4, 0],
        [0.2, 0.01]
    ])
    E = Matrix.unit(2)
    b = Matrix.vector([0.8, 0.43])

    simple_iteration_test(E - A, b)
    gauss_zeidel_test(A, b)

    print("-------------")
    print("All tests: OK")
