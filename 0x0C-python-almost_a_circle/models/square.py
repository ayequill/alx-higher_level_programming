#!/usr/bin/python3
"""
Module for a Square class
"""
from rectangle import Rectangle


class Square(Rectangle):
    """
    A Square class

    Args:
        Rectangle (class): Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        Size getter
        """
        return self.height

    @size.setter
    def size(self, value):
        """
        Size setter

        Args:
            value (int): size of square
        """
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
        Updates the instance with new value
        """
        if args and len(args) > 0:
            arg_li = (
                'id',
                'size',
                'x',
                'y'
            )

            for arg in range(len(args)):
                setattr(self, arg_li[arg], args[arg])

        if kwargs and len(kwargs.keys()) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the instance

        Returns:
            dict: dictionary of the instance
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y,
        }
