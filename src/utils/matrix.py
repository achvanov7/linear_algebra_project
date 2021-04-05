from random import randint, random
from accuracy import *


class Matrix:

    @staticmethod
    def zero(n, m):
        return Matrix([[0] * m for _ in range(n)])

    @staticmethod
    def diagonal(diag):

        def get_row(i):
            return [0] * i + [diag[i]] + [0] * (n - i - 1)

        n = len(diag)
        return Matrix([get_row(i) for i in range(n)])

    @staticmethod
    def unit(n):
        return Matrix.diagonal([1] * n)

    @staticmethod
    def vector(a):
        return Matrix([[i] for i in a])

    @staticmethod
    def random(n, m, precision=16):
        result = Matrix.zero(n, m)
        for i in range(n):
            for j in range(m):
                result[i][j] = random()
        return result.prec(precision)

    @staticmethod
    def randint(n, m, first=0, last=1):
        result = Matrix.zero(n, m)
        for i in range(n):
            for j in range(m):
                result[i][j] = randint(first, last)
        return result

    def __init__(self, data):
        if len(data) == 0:
            raise ValueError('Matrix must have columns')
        if len(data[0]) == 0:
            raise ValueError('Matrix must have rows')

        self.height = len(data)
        self.width = len(data[0])

        if [len(line) for line in data].count(self.width) != self.height:
            raise ValueError('Matrix must be rectangular')

        self.data = data

    def map(self, fun):
        result = Matrix.zero(self.height, self.width)
        for i in range(self.height):
            result[i] = list(map(fun, self[i]))
        return result

    def copy(self):
        return self.map(lambda x: x)

    def prec(self, p=3):
        return self.map(lambda x: int(x * 10 ** p) / 10 ** p)

    def fix_zeros(self):
        return self.map(lambda x: 0 if eq(x, 0) else x)

    def __str__(self):

        def shift(x):
            return ' ' * (offset - len(x)) + x

        str_data = self.map(str)
        offset = max([max(map(len, line)) for line in str_data])
        str_data = [' '.join(map(shift, line)) for line in str_data]
        return '\n'.join(str_data)

    def __repr__(self):
        return str(self)

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        if len(value) != self.width:
            raise ValueError('Matrix has to be rectangular')

        self.data[key] = value

    def __eq__(self, other):
        if self.height != other.height or self.width != other.width:
            return False
        for i in range(self.height):
            for j in range(self.width):
                if not eq(self[i][j], other[i][j]):
                    return False
        return True

    def __rmul__(self, n):
        result = Matrix.zero(self.height, self.width)
        for i in range(self.height):
            for j in range(self.width):
                result[i][j] = self[i][j] * n
        return result

    def __neg__(self):
        return -1 * self

    def __add__(self, other):
        if self.height != other.height or self.width != other.width:
            raise ValueError('Dimensions of the matrices have to be the same')

        result = Matrix.zero(self.height, self.width)
        for i in range(self.height):
            for j in range(self.width):
                result[i][j] = self[i][j] + other[i][j]
        return result

    def __sub__(self, other):
        return self + -other

    def __iadd__(self, other):
        self = self + other
        return self

    def __isub__(self, other):
        self = self - other
        return self

    def __mul__(self, other):
        if self.width != other.height:
            raise ValueError('Dimensions of the matrices must be suitable')

        result = Matrix.zero(self.height, other.width)
        for i in range(result.height):
            for j in range(result.width):
                for k in range(self.width):
                    result[i][j] += self[i][k] * other[k][j]
        return result

    def __imul__(self, other):
        self = self * other
        return self

    def __pow__(self, n):
        if type(n) != int:
            raise TypeError('Argument has to be of the type int')
        if n < 0:
            raise ValueError('Argument has to be a non-negative number')

        result = Matrix.unit(self.height)
        while n > 0:
            if n % 2 == 1:
                result *= self
            self *= self
            n //= 2
        return result

    def norm(self):
        result = 0
        for i in range(self.height):
            for j in range(self.width):
                result += abs(self[i][j]) ** 2
        return result ** 0.5

    def normalize(self):
        norm = self.norm()
        if eq(norm, 0):
            return self
        return (1 / norm) * self

    def transpose(self):
        result = Matrix.zero(self.width, self.height)
        for i in range(self.height):
            for j in range(self.width):
                result[j][i] = self[i][j]
        return result

    def gershgorin_circles(self):
        self.square()
        result = [(0, 0)] * self.height
        for i in range(self.height):
            result[i] = (self[i][i], sum(map(abs, self[i])) - abs(self[i][i]))
        return result

    def circle_check(self, eps=global_eps):
        for cent, rad in self.gershgorin_circles():
            if rad > eps:
                return False
        return True

    def square(self):
        if self.height != self.width:
            raise ValueError('Matrix must be a square')

    def symmetric(self):
        if self != self.transpose():
            raise ValueError('Matrix must be symmetric')

    def tridiagonal(self):
        fail = False
        for i in range(self.height):
            for j in range(self.width):
                if abs(i - j) > 1 and not eq(self[i][j], 0):
                    fail = True
                    break
        if fail:
            raise ValueError('Matrix must be tridiagonal')
