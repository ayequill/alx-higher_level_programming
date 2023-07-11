#!/usr/bin/python3
"""
A module that contains Student class
"""


class Student:
    """
    A Student class
    """

    def __init__(self, first_name, last_name, age):
        """
        Constructor for Student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns dictionary representation of an
        instance
        """
        return self.__dict__
