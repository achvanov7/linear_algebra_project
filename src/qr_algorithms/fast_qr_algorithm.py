from src.utils import *
from src.tridiagonal import *
from src.qr_algorithms.qr_algorithm import fix_aq as def_fix


def fix_aq(A, Q):
    L = A[-2][-2], A[-2][-1], A[-1][-2], A[-1][-1]
    D = (L[0] - L[3]) ** 2 + 4 * L[1] * L[2]
    D **= 0.5
    x = (L[0] + L[3] + D) / 2, (L[0] + L[3] - D) / 2

    if abs(x[0] - L[3]) < abs(x[1] - L[3]):
        v = x[0]
    else:
        v = x[1]

    E = Matrix.unit(A.width)
    A -= v * E
    A, Q = def_fix(A, Q, qr_tridiagonal)
    A += v * E
    return A, Q


def fix_eigens(eigens, A, eps):
    bottom, right = 0, 0
    for i in range(A.width - 1):
        bottom += abs(A[-1][i])
        right += abs(A[i][-1])

    if bottom < eps and right < eps:
        eigens.append(A[-1][-1])
        A = Matrix([A[i][:-1] for i in range(A.width - 1)])
    return A


def fast_qr_algo(A, eps=global_eps):
    A.square()
    A.symmetric()
    A.tridiagonal()

    eigens = []
    Q = Matrix.unit(A.width)

    while A.width > 1:
        A, Q = fix_aq(A, Q)
        A = fix_eigens(eigens, A, eps)
    eigens.append(A[0][0])
    eigens = eigens[::-1]
    return eigens, Q
