#!/usr/bin/python3
"""
Module that contains a Rectangle class
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    A rectangle class
    """
    def __init__(self, width, height):

        """
        The __init__ function takes in three arguments:
        self, width and height.
        self refers to the instance of the class (Rectangle).
        width and height are both integers that represent
        the dimensions of a rectangle.

        :param self: Refer to the class itself
        :param width: Set the width of the rectangle
        :param height: Set the height of the rectangle
        :return: An instance of the class
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
