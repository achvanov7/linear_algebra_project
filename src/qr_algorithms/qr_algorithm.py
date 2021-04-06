from src.utils import *
from src.givens_rotation import *


def fix_aq(A, Q, qr_dec):
    Qk, Rk = qr_dec(A)
    if type(Qk) == Matrix:
        A = Rk * Qk
        Q *= Qk
    else:
        A = Rk
        for (i, j, c, s) in Qk:
            givens_mul_right(A, i, j, c, s)
            givens_mul_right(Q, i, j, c, s)
    return A, Q


def qr_algo(A, eps=global_eps, qr_dec=qr_givens):
    A.square()
    A.symmetric()

    Q = Matrix.unit(A.width)

    while not A.circle_check(eps):
        A, Q = fix_aq(A, Q, qr_dec)

    eigens = [A[i][i] for i in range(A.width)]
    return eigens, Q
