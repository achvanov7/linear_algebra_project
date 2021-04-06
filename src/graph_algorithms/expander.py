from src.utils import *
from src.tridiagonal import *
from src.qr_algorithms import *


def build_nxn(n):
    A = Matrix.zero(n * n, n * n)

    def num(i, j):
        i %= n
        j %= n
        return i + j * n

    for x in range(n):
        for y in range(n):
            v = num(x, y)
            for i, j in [
                (x + 2 * y, y),
                (x - 2 * y, y),
                (x + (2 * y + 1), y),
                (x - (2 * y + 1), y),
                (x, y + 2 * x),
                (x, y - 2 * x),
                (x, y + (2 * x + 1)),
                (x, y - (2 * x + 1))
            ]:
                u = num(i, j)
                A[v][u] += 1
                A[u][v] += 1
    return A


def build_p_inf(p):
    A = Matrix.zero(p + 1, p + 1)

    def rev(x):
        if x == 0:
            return p
        if x == p:
            return 0
        n = p - 2
        res = 1
        while n > 0:
            if n % 2 == 1:
                res = (res * x) % p
            x = (x * x) % p
            n //= 2
        return res

    def inc(x):
        if x == p:
            return p
        return (x + 1) % p

    def dec(x):
        if x == p:
            return p
        return (x + 1) % p

    for x in range(p + 1):
        for y in [inc(x), dec(x), rev(x)]:
            A[x][y] += 1
            A[y][x] += 1
    return A


def count_alpha(A, eps=1e-5):
    B, _ = tridiagonalize(A)
    eigens, _ = fast_qr_algo(B, eps)
    eigens = sorted(eigens, reverse=True)
    deg = sum(A[0])
    lam = max(abs(eigens[1]), abs(eigens[-1]))
    return lam / deg
