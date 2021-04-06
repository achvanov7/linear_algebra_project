from src.utils import *
from src.givens_rotation.multiplication import *


def find_ne_zero(A, j):
    k = j
    while k < A.width and eq(A[k][j], 0):
        k += 1
    return k


def fix_qr(Q, R, j, n):
    k = find_ne_zero(R, j)
    if k == n:
        return

    if k != j:
        givens_mul(Q, j, k, 0, 1)
        givens_mul(R, j, k, 0, 1)

    for i in range(j + 1, n):
        c = 1 / (1 + R[i][j] ** 2 / R[j][j] ** 2) ** 0.5
        s = R[i][j] / R[j][j] * c

        givens_mul(Q, j, i, c, s)
        givens_mul(R, j, i, c, s)


def qr_givens(A):
    A.square()
    n = A.width

    Q = Matrix.unit(n)
    R = A.copy()

    for j in range(n - 1):
        fix_qr(Q, R, j, n)

    Q = Q.transpose()
    R = R.fix_zeros()
    return Q, R
