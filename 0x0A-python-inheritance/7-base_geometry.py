#!/usr/bin/python3
"""
Module containing BaseGeometry Class
"""


class BaseGeometry:
    """
    BaseGeometry class
    """

    def __init__(self):
        """
        Constructor
        """
        pass

    def area(self):
        """
        Validates the area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates integers
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")