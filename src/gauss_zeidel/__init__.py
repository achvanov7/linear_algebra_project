from src.utils import *

threshold = 20


def check_diag(A):
    return [A[i][i] for i in range(A.width)] == [0] * A.width


def LU_decomposition(A):
    L = Matrix.zero(A.height, A.width)
    U = Matrix.zero(A.height, A.width)
    for i in range(A.height):
        for j in range(i + 1):
            L[i][j] = A[i][j]
        for j in range(i + 1, A.width):
            U[i][j] = A[i][j]
    return L, U


def Lx_solve(L, b):
    x = Matrix.zero(L.width, 1)
    for i in range(L.width):
        prefix = 0
        for j in range(i):
            prefix += L[i][j] * x[j][0]
        x[i][0] = (b[i][0] - prefix) / L[i][i]
    return x


def gauss_zeidel(A, b, eps=global_eps):
    if check_diag(A):
        return 0

    L, U = LU_decomposition(A)
    U = -U
    x = Matrix.random(A.width, 1)
    count_fail_iters = 0

    while (A * x - b).norm() >= eps:
        x_new = Lx_solve(L, U * x + b)

        if abs(x.norm() - x_new.norm()) >= 1:
            count_fail_iters += 1
        else:
            count_fail_iters = 0

        x = x_new

        if count_fail_iters > threshold:
            return 0

    return x
