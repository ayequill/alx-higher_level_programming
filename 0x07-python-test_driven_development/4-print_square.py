#!/usr/bin/python3
"""
This module contains a function that prints a square
"""


def print_square(size):
    """
    Prints a square

    Args:
        size (int): size of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    if not isinstance(size, int) or (not isinstance(size, int) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()