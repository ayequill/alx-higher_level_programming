#!/usr/bin/python3
"""
This module contains a function that prints first_name and last_name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the first and last name

    Args:
        first_name (str): first name
        last_name (str, optional): last name. Defaults to "".

    Raises:
        TypeError: if either args is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
