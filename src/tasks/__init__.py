from src.utils import *
from src.simple_iteration import *
from src.gauss_zeidel import *
from src.givens_rotation import *
from src.householder_transformation import *
from src.qr_algorithms import *
from src.tridiagonal import *
from src.graph_algorithms import *


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


def task_5():
    A = input_matrix()
    v = input_vector()
    HA = householder_mul(A, v)
    print_ans([
        ("Hv * A", HA)
    ])


def task_6():
    A = input_matrix()
    Q, R = qr_householder(A)
    print_ans([
        ("Q", Q),
        ("R", R)
    ])


def task_7():
    A = input_matrix()
    x = input_vector()
    eps = input_accuracy()
    res = simple_iteration(A, x, eps)
    if res == 0:
        print_ans([
            ("Fail", 0)
        ])
    else:
        k, v = res
        print_ans([
            ("Eigen Value", k),
            ("Eigen Vector", v)
        ])


def task_8():
    A = input_matrix()
    eps = input_accuracy()
    eigens, Q = qr_algo(A, eps)
    print_ans([
        ("Eigen Values", eigens),
        ("Q_k", Q)
    ])


def task_9():
    A = input_matrix()
    B, Q = tridiagonalize(A)
    print_ans([
        ("A'", B),
        ("Q", Q)
    ])


def task_10():
    A = input_matrix()
    eps = input_accuracy()
    eigens, Q = qr_algo(A, eps, qr_tridiagonal)
    print_ans([
        ("Eigen Values", eigens),
        ("Q_k", Q)
    ])


def task_11():
    A = input_matrix()
    eps = input_accuracy()
    eigens, Q = fast_qr_algo(A, eps)
    print_ans([
        ("Eigen Values", eigens),
        ("Q_k", Q)
    ])


def task_12():
    A = input_matrix()
    B = input_matrix()
    res = check_isomorphism(A, B)
    print_ans([
        ("Isomorphism result", res)
    ])


def task_13():
    print("Enter two numbers - n, p: ")
    n, p = map(int, input().split())
    a1 = count_alpha(build_nxn(n))
    a2 = count_alpha(build_p_inf(p))
    print_ans([
        ("alpha_1", a1),
        ("alpha_2", a2),
    ])


all_tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10, task_11, task_12, task_13]


def run_all_tasks():
    for i in range(len(all_tasks)):
        print(f"Task {i + 1}:")
        all_tasks[i]()
        print("-------\n")
