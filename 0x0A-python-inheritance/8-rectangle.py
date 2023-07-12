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
        The __init__ function takes in three arguments: self, width and height.
        self refers to the instance of the class (Rectangle).
        width and height are both integers that represent the dimensions of a rectangle.

        :param self: Refer to the class itself
        :param width: Set the width of the rectangle
        :param height: Set the height of the rectangle
        :return: An instance of the class
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height


r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))