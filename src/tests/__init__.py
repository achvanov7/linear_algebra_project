from src.utils import *
from src.simple_iteration import *
from src.gauss_zeidel import *
from src.givens_rotation import *
from src.householder_transformation import *
import random

eps = 1e-14


def simple_iteration_method_test(A, b):
    x = simple_iteration_method(A, b, eps)
    assert (x == A * x + b)
    print("Simple Iteration Method test: OK")


def gauss_zeidel_test(A, b):
    x = gauss_zeidel(A, b, eps)
    assert (A * x == b)
    print("Gauss-Zeidel test: OK")


def qr_dec_test(A, qr_dec):
    Q, R = qr_dec(A)
    if type(Q) != Matrix:
        tmp = Q
        Q = Matrix.unit(A.width)
        for (i, j, c, s) in tmp:
            givens_mul_right(Q, i, j, c, s)

    assert (Q * (Q.transpose()) == Matrix.unit(Q.width))

    for i in range(R.height):
        for j in range(i):
            assert (eq(R[i][j], 0))

    assert (Q * R == A)
    print(f"{qr_dec.__name__} test: OK")


def simple_iteration_test(A):
    x = Matrix.random(A.width, 1)
    k, v = simple_iteration(A, x, eps)
    assert (A * v == k * v)
    print("Simple Iteration test: OK")


def run_all_tests():
    A = Matrix([
        [0.4, 0],
        [0.2, 0.01]
    ])
    E = Matrix.unit(2)
    b = Matrix.vector([0.8, 0.43])

    simple_iteration_method_test(E - A, b)
    gauss_zeidel_test(A, b)

    A = Matrix([
        [0, 1, 1],
        [1, 0, 1],
        [0, 1, 0]
    ])
    qr_dec_test(A, qr_givens)
    qr_dec_test(A, qr_householder)
    simple_iteration_test(A)

    print("-------------")
    print("All tests: OK")
