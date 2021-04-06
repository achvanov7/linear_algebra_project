from src.utils import *
from src.simple_iteration import *
from src.gauss_zeidel import *
from src.givens_rotation import *
from src.householder_transformation import *
from src.qr_algorithms import *
from src.tridiagonal import *
from src.graph_algorithms import *
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


def qr_algo_test(A, qr_dec=qr_givens):
    ev, Q = qr_algo(A, eps, qr_dec)

    for i in range(Q.width):
        e_vector = Matrix.vector([Q[j][i] for j in range(Q.height)])
        assert (A * e_vector == ev[i] * e_vector)
    print(f"QR Algorithm {qr_dec.__name__} test: OK")


def tridiagonalization_test(A):
    B, Q = tridiagonalize(A)
    B.tridiagonal()
    assert (Q.transpose() * A * Q == B)
    return B


def fast_qr_algo_test(A):
    ev, Q = fast_qr_algo(A, eps)

    for i in range(Q.width):
        e_vector = Matrix.vector([Q[j][i] for j in range(Q.height)])
        assert (A * e_vector == ev[i] * e_vector)
    print("Fast QR Algorithm test: OK")


def gen_random_shuffle_matrix(n):
    p = [i for i in range(n)]
    random.shuffle(p)
    P = Matrix.zero(n, n)
    rP = Matrix.zero(n, n)
    for i in range(n):
        P[i][p[i]] = 1
        rP[p[i]][i] = 1
    assert (P * rP == Matrix.unit(n))
    return P, rP


def shuffle_matrix(A):
    P, rP = gen_random_shuffle_matrix(A.width)
    return P * A * rP


def isomorphism_test(A, B, exp):
    assert (check_isomorphism(A, A) == 1)
    assert (check_isomorphism(B, B) == 1)
    assert (check_isomorphism(A, B) == exp)
    C = shuffle_matrix(A)
    assert (check_isomorphism(A, C) == 1)
    C = shuffle_matrix(B)
    assert (check_isomorphism(B, C) == 1)

    print("Isomorphism test: OK")


def expanders_test():
    A = build_nxn(2)
    assert (eq(count_alpha(A), 0.5))
    A = build_p_inf(2)
    assert (eq(count_alpha(A), 0.57735027))
    print("Expanders test: OK")


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

    A = Matrix([
        [4, 1, 1, 0, 0],
        [1, -1.1, 1, 2, -1],
        [1, 1, -3, 0.02, 0.02],
        [0, 2, 0.02, 0, 5],
        [0, -1, 0.02, 5, -1]
    ])

    qr_algo_test(A)
    B = tridiagonalization_test(A)
    qr_dec_test(B, qr_tridiagonal)
    qr_algo_test(B, qr_tridiagonal)
    fast_qr_algo_test(B)

    C = Matrix([
        [1, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0],
        [0, 0, 1, 0, 0, 1],
        [0, 0, 1, 0, 0, 1],
        [0, 0, 0, 1, 1, 0]
    ])
    D = Matrix([
        [0, 1, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 0]
    ])

    isomorphism_test(C, D, 0)

    expanders_test()

    print("-------------")
    print("All tests: OK")
