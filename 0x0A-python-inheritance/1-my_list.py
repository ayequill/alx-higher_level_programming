#!/usr/bin/python3
"""
A module that contains a function that prints elements in
a list from a subclass in ascending order
"""


class MyList(list):
    """
    A class that extends the list class
    """

    def print_sorted(self):
        """
        Prints elements in the class in sorted order
        """
        sorted_list = sorted(self)
        print(sorted_list)
