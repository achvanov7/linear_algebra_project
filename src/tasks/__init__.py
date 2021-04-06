from src.utils import *
from src.simple_iteration import *
from src.gauss_zeidel import *


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


all_tasks = [task_1, task_2]


def run_all_tasks():
    for i in range(len(all_tasks)):
        print(f"Task {i + 1}:")
        all_tasks[i]()
        print("-------\n")
