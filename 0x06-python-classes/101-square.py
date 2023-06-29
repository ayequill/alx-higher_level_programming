#!/usr/bin/python3
"""
This is a module that contains a Square class
"""


class Square:
    """
    This is a Square class
    """

    def __init__(self, size: int = 0, position: tuple = (0, 0)):
        """
        Initializing the class

        Args:
            size (int): size of the square
            position (tuple): position of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or len(position) != 2 or \
                not all(isinstance(num, int) and num >= 0 for num in position):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

    def __str__(self):
        return self.my_print()

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

    @property
    def position(self) -> tuple:
        """
        a getter for the position of the square

        Returns:
            tuple: position of the square
        """
        return self.__position

    @position.setter
    def position(self, pos):
        """
        a setter for the position of the square

        Args:
            pos (tuple): position of the square
        """
        if (not isinstance(pos, tuple) or len(pos) != 2
            or not all(isinstance(num, int) and num >= 0
                       for num in pos)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = pos

    def area(self):
        """
        returns the area of the square
        """
        return self.__size ** 2

    def my_print(self) -> str:
        """
        Returns the square as a string representation.
        """
        result = ""
        if self.__size == 0:
            return result

        for _ in range(self.__position[1]):
            result += "\n"

        for _ in range(self.__size):
            # Number of spaces for horizontal position
            indent = " " * self.__position[0]
            line = "#" * self.__size  # Line with '#' characters
            result += f"{indent}{line}\n"
        return result
