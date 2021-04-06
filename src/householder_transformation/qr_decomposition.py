from src.utils import *
from src.householder_transformation.multiplication import *


def fix_qr(Q, R, j, n):
    u = Matrix.vector([
        0 if i < j else R[i][j] for i in range(n)
    ]).normalize()

    e_j = Matrix.vector([int(i == j) for i in range(n)])

    v = (u - e_j).normalize()

    Q = householder_mul(Q, v)
    R = householder_mul(R, v)
    return Q, R


def qr_householder(A):
    A.square()
    n = A.width

    Q = Matrix.unit(n)
    R = A.copy()

    for j in range(n):
        Q, R = fix_qr(Q, R, j, n)

    Q = Q.transpose()
    R = R.fix_zeros()
    return Q, R
