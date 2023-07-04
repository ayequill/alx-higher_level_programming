#!/usr/bin/python3
"""
This module contains a Rectangle Class
"""


class Rectangle:
    """
    A class representing a Rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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

    def perimeter(self) -> float:
        """
        Return the perimeter of the Rectangle

        Returns:
            float: return the perimeter of the Rectangle
        """
        return (2 * (self.__height + self.__width)
                if all(x != 0 for x in (self.__height, self.__width))
                else 0)

    def area(self) -> float:
        """
        Return the area of the Rectangle

        Returns:
            float: return the area of the Rectangle
        """
        return self.__height * self.__width

    def __str__(self) -> str:
        """
        Return a string representation of the Rectangle

        Returns:
            str: returns a string representation of the Rectangle
            with # characters
        """
        if any(x == 0 for x in (self.__height, self.__width)):
            return ''
        rectangle_str_rep = ''

        for col in range(self.__height):
            for _ in range(self.__width):
                rectangle_str_rep += f"{self.print_symbol}"

            if col < self.__height - 1:
                rectangle_str_rep += "\n"
        return rectangle_str_rep

    def __repr__(self) -> str:
        """
        A string representation of the object
        Returns:
            _str_: rectangle dimensions
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a deletion of the object
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns comparison between rect_1 and rect_2

        Args:
            rect_1 (Rectangle): An instance of Rectangle
            rect_2 (Rectangle): An instance of Rectangle

        Raises:
            TypeError: if rect_1 and rect_2 are not of
            Rectangle

        Returns:
            Rectangle: Rectangle object
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
