from src.utils import *


def givens_mul(A, i, j, c, s):
    n = A.width
    new_i, new_j = [0] * n, [0] * n
    for k in range(n):
        new_i[k] = c * A[i][k] + s * A[j][k]
        new_j[k] = c * A[j][k] - s * A[i][k]
    A[i], A[j] = new_i[:], new_j[:]


def givens_mul_right(A, i, j, c, s):
    n = A.width
    new_i, new_j = [0] * n, [0] * n
    for k in range(n):
        new_i[k] = c * A[k][i] - s * A[k][j]
        new_j[k] = c * A[k][j] + s * A[k][i]
    for k in range(n):
        A[k][i], A[k][j] = new_i[k], new_j[k]
