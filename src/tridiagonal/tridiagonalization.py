from src.utils import *
from src.householder_transformation import *


def tridiagonalize_next(j, n, B, Q):
    u = Matrix.zero(n, 1)
    for i in range(j + 1, n):
        u[i][0] = B[i][j]

    if eq(u.norm(), 0):
        return B, Q

    u = u.normalize()
    e = Matrix.zero(n, 1)
    e[j + 1][0] = 1
    v = u - e

    if eq(v.norm(), 0):
        return B, Q

    v = v.normalize()
    B = householder_mul(B, v)
    B = householder_mul_right(B, v)
    Q = householder_mul(Q, v)
    return B, Q


def tridiagonalize(A):
    A.square()
    A.symmetric()

    n = A.width

    B = A.copy()
    Q = Matrix.unit(n)

    for j in range(n - 1):
        B, Q = tridiagonalize_next(j, n, B, Q)

    Q = Q.transpose()
    B = B.fix_zeros()

    return B, Q
