#!/usr/bin/python3
"""
This module contains a function that divides a matrix of numbers
"""


def matrix_divided(matrix, div):
    """
    This function divides a matrix of numbers

    Args:
        matrix (list): a matrix of numbers
        div (int): number
    Raises:
        - matrix must be a list of lists of integers
        or floats, otherwise a TypeError is raised.
        - if each row of matrix is not the same size we raise a TypeError
        - if div is not an integer or float we raise a TypeError
        - if div is 0 we raise a ZeroDivisionError
    Returns:
        list: a matrix of quotients
    """
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for li in matrix:
        if (not isinstance(li, list)
            or any(not isinstance(num, (float, int))
                   for num in li)):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

        if len(li) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(num/div, 2) for num in row] for row in matrix]
