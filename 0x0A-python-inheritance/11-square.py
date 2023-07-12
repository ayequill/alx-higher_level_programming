#!/usr/bin/python3
"""
Module that contains a Rectangle class
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A rectangle class
    """
    def __init__(self, size):

        """
        Initializing the square class
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """
        returns a string representation of the square
        """
        return f"[Square] {self.__size}/{self.__size}"
