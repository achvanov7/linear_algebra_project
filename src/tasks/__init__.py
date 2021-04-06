from src.utils import *
from src.simple_iteration import *
from src.gauss_zeidel import *
from src.givens_rotation import *


def print_ans(x):
    print("Answer:")
    for name, val in x:
        print(f"{name} = \n{val}")


def task_1():
    A = input_matrix()
    b = input_vector()
    eps = input_accuracy()
    x = simple_iteration_method(A, b, eps)
    print_ans([
        ("x", x)
    ])


def task_2():
    A = input_matrix()
    b = input_vector()
    eps = input_accuracy()
    x = gauss_zeidel(A, b, eps)
    print_ans([
        ("x", x)
    ])


def task_3():
    A = input_matrix()
    print("Enter the two indexes: ")
    i, j = map(int, input().split())
    print("Enter the c and s numbers: ")
    c, s = map(float, input().split())
    givens_mul(A, i, j, c, s)
    print_ans([
        (f"G({i}, {j}, {c}, {s}) * A", A)
    ])


def task_4():
    A = input_matrix()
    Q, R = qr_givens(A)
    print_ans([
        ("Q", Q),
        ("R", R)
    ])


all_tasks = [task_1, task_2, task_3, task_4]


def run_all_tasks():
    for i in range(len(all_tasks)):
        print(f"Task {i + 1}:")
        all_tasks[i]()
        print("-------\n")
