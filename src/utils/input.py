from src.utils.matrix import *


def input_matrix():
    print("Enter the matrix's dimensions: ")
    n, m = map(int, input().split())

    print("Enter the matrix: ")
    result = [0] * n
    for i in range(n):
        result[i] = list(map(float, input().split()))

    return Matrix(result)


def input_vector():
    print("Enter the size of the vector: ")
    n = int(input())

    print("Enter the vector (one number each line): ")
    result = [0] * n
    for i in range(n):
        result[i] = float(input())

    return Matrix.vector(result)


def input_accuracy():
    print("Enter the accuracy: ")
    accuracy = float(input())
    return accuracy
