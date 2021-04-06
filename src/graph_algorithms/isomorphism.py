from src.qr_algorithms import *
from src.tridiagonal import *
from src.utils import *


def check_degrees(A, B):
    a = sorted([(sum(A[i]), A[i][i]) for i in range(A.width)])
    b = sorted([(sum(B[i]), B[i][i]) for i in range(B.width)])
    return a == b


def get_eigens(A):
    eigens, _ = fast_qr_algo(A)
    return sorted(eigens)


def check_eigens(A, B):
    a, b = get_eigens(A), get_eigens(B)
    for i in range(len(a)):
        if not eq(a[i], b[i]):
            return False
    return True


def dfs(v, A, used):
    used[v] = True
    cnt_v = 1
    cnt_e = sum(A[v])
    for u in range(A.width):
        if A[v][u] == 1 and not used[u]:
            cv, ce = dfs(u, A, used)
            cnt_e += ce
            cnt_v += cv
    return cnt_v, cnt_e


def get_comp(A):
    n = A.width
    used = [False] * n
    cnt = []
    for i in range(n):
        if not used[i]:
            cnt.append(dfs(i, A, used))
    return sorted(cnt)


def check_comp(A, B):
    return get_comp(A) == get_comp(B)


def check_isomorphism(A, B):
    A.square()
    A.symmetric()
    B.square()
    B.symmetric()

    if A == B:
        return 1

    if A.width != B.width:
        return 0

    if not check_degrees(A, B):
        return 0

    AT, _ = tridiagonalize(A)
    BT, _ = tridiagonalize(B)

    if not check_eigens(AT, BT):
        return 0

    if not check_comp(A, B):
        return 0

    return 1
