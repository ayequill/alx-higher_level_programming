#!/usr/bin/python3
"""
This is a module that contains a Square class
"""


class Square:
    """
    This is a Square class
    """

    def __init__(self, size: int = 0):
        """
        Initializing the class

        Args:
            size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        returns the area of the square
        """
        return self.__size ** 2
