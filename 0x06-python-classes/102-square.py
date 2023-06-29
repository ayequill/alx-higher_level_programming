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
        self.__size = size

    @property
    def size(self) -> int:
        """
        a getter for the size of the square

        Returns:
            int: size of the square
        """
        return self.__size

    @size.setter
    def size(self, size: int):
        """
        a setter for the size of the square

        Args:
            size (int): size of the square

        Raises:
            TypeError: if the size of the square is not a number
            ValueError: if the size of the square is not greater 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self) -> int:
        """
        returns the area of the square
        """
        return self.__size ** 2

    def __lt__(self, other) -> bool:
        """
        overriding the < operator

        Args:
            other (_Square_): the other square object
        """
        return self.area() < other.area()

    def __le__(self, other) -> bool:
        """
        overriding the <= operator

        Args:
            other (_Square_): the other square object
        """
        return self.area() <= other.area()

    def __eq__(self, other) -> bool:
        """
        overriding the == operator

        Args:
            other (_Square_): the other square object
        """
        return self.area() == other.area()

    def __gt__(self, other) -> bool:
        """
        overriding the > operator

        Args:
            other (_Square_): the other square object
        """
        return self.area() > other.area()

    def __ge__(self, other) -> bool:
        """
        overriding the >= operator

        Args:
            other (_Square_): the other square object
        """
        return self.area() >= other.area()
