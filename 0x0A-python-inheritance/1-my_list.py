#!/usr/bin/python3
"""
A module that contains a function that prints
elements in
a list
"""


class MyList(list):
    """
    MyList class
    """

    def __int__(self):

        """
        initializing and extending the parent class
        """
        super().__init__()

    def print_sorted(self):
        """
        Prints elements in the class in sorted
        order
        """
        print(sorted(self.copy()))
