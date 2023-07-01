#!/usr/bin/python3
"""
This module contains a function that adds two numbers
"""


def add_integer(a, b=98):
    """Adds two numbers
    Args:
        a (int, float): number as argument
        b (int, optional): number as argument

    Raises:
        TypeError: a and b must be integers or floats

    Returns:
        int: the sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
