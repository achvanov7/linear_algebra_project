from src.utils import *


def householder_mul(A, v):
    return A - (2 * v) * (v.transpose() * A)


def householder_mul_right(A, v):
    return A - (A * (2 * v)) * v.transpose()
