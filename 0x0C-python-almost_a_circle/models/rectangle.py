#!/usr/bin/python3
"""
Module for rectangle class
"""
from base import Base


class Rectangle(Base):
    """
    A Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):

        """
        The __init__ function is a constructor for
        the Rectangle class.
        It initializes all the attributes of an
        instance, including id, width, height, x and y.

        :param self: Refer to the instance of the class
        :param width: Set the width of the rectangle
        :param height: Set the height of the rectangle
        :param x: Set the x value of the rectangle
        :param y: Set the y value of the rectangle
        :param id: Assign an id to the object
        :return: Nothing
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self) -> int:
        """
        Returns the width
        """
        return self.__width

    @width.setter
    def width(self, value) -> None:
        """
        Sets the width
        """
        if type(value) == int:
            raise TypeError("must be an integer")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height
        """
        return self.__height

    @height.setter
    def height(self, value) -> None:
        """
        Sets the height
        """
        if type(value) == int:
            raise TypeError("must be an integer")
        self.__height = value

    @property
    def x(self):
        """
        Gets the x value
        """
        return self.__x

    @x.setter
    def x(self, value) -> None:
        """
        Sets the x value
        """
        if type(value) == int:
            raise TypeError("must be an integer")
        self.__x = value

    @property
    def y(self):
        """
        Gets the y value
        """
        return self.__y

    @y.setter
    def y(self, value) -> None:
        """
        Sets y value
        """
        if type(value) == int:
            raise TypeError("must be an integer")
        self.__y = value
