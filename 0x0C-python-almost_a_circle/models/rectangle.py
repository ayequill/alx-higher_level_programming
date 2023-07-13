#!/usr/bin/python3
"""
Module for rectangle class
"""
from base import Base


class Rectangle(Base):
    """
    A Rectangle class
    """
    # TODO
    # @classmethod
    # def raise_err(cls, name, **kwargs):
    #     err_msg = {
    #         "not-int": "must be an integer",
    #         "negative": "must be > 0",
    #         "negative_alt": "must be >= 0"
    #     }
    #     for key, value in kwargs.items():
    #         if value in err_msg:
    #             raise key(name + err_msg[value])

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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Width setter
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height value
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """
        Gets the x value
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the x value
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """
        y getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the y value
        """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self) -> int:
        """
        The area function returns the area of a rectangle.

        :param self: Refer to the instance of the class
        :return: The area of the rectangle
        """
        return self.__width * self.__height

    def display(self):

        """
        The display function prints the rectangle
        with the character #

        :param self: Reference the object itself
        :return: None
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x, "#" * self.__width)

    def __str__(self):
        """
        Returns a string rep of the rectangle instance
        Returns:
            str: rectangle 
        """
        return f"[Rectangle] ({self.id}) \
            {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    
    def update(self, *args, **kwargs):
        """
        Updates the instance with new value
        """
        if args and len(args) > 0:
            arg_li = (
                'id',
                'width',
                'height',
                'x',
                'y'
            )

            for arg in range(len(args)):
                setattr(self, arg_li[arg], args[arg])
        
        if kwargs and len(kwargs.keys()) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)


if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(10, height=1)
    print(r1)

    r1.update(width=1, x=2)
    print(r1)

    r1.update(y=1, width=2, x=3, id=89)
    print(r1)

    r1.update(x=1, height=2, y=3, width=4)
    print(r1)