from src.utils import *
from src.givens_rotation import *


def find_non_zero(j, n, R):
    k = j
    while k < n and eq(R[k][j], 0):
        k += 1
    return k


def fix_qr(j, n, Q, R):
    k = find_non_zero(j, n, R)
    if k == n:
        return
    if k != j:
        Q.append((j, k, 0, 1))
        givens_mul(R, j, k, 0, 1)

    for i in range(j + 1, n):
        c = 1 / (1 + R[i][j] ** 2 / R[j][j] ** 2) ** 0.5
        s = R[i][j] / R[j][j] * c

        Q.append((j, i, c, s))
        givens_mul(R, j, i, c, s)


def qr_tridiagonal(A):
    A.square()
    A.symmetric()
    A.tridiagonal()

    n = A.width

    Q = []
    R = A.copy()

    for j in range(n - 1):
        fix_qr(j, n, Q, R)

    Q = [(i, j, c, -s) for (i, j, c, s) in Q]
    R = R.fix_zeros()
    return Q, R
