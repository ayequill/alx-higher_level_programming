#!/usr/bin/python
""" Prints a matrix of integers """


def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print("{}".format(matrix[i][j]), end=" ")
            print()
