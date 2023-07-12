#!/usr/bin/python3
"""
A module for MyList class
"""


class MyList(list):
    """
    MyList class
    """
    def print_sorted(self):
        """
        Prints elements in the class in sorted
        order
        """
        sorted_li = super().copy()
        sorted_li.sort()
        print(sorted_li)
