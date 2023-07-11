#!/usr/bin/python3
"""
A module that contains a function that prints elements in
a list from a subclass in ascending order
"""


class MyList(list):
    """
    MyList class
    """

    def print_sorted(self):
        """
        Prints elements in the class in sorted order
        """
        print(sorted(self))
