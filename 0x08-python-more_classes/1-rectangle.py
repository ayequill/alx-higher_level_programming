#!/usr/bin/python3
"""
This module contains a Rectangle Class
"""


class Rectangle:
    """
    A class representing a Rectangle
    """

    def __init__(self, width: int = 0, height: int = 0):
        """
        Initializing the Rectangle class

        Args:
            width (int): width of the Rectangle
            height (int): height of the Rectangle
        """

        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if height < 0:
            raise ValueError("height must be >= 0")

        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self) -> int:
        """
        Getter for the width of the Rectangle

        Returns:
            int: return the width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value: int):
        """
        Setter for the width of the Rectangle

        Args:
            value (int): new width of the Rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self) -> int:
        """
        Getter for the height of the Rectangle

        Returns:
            int: return the height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value: int):
        """
        Setter for the height of the Rectangle

        Args:
            value (int): new height of the Rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
