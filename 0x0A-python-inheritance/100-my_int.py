#!/usr/bin/python3
"""
Module that contains MyInt class
"""


class MyInt(int):
    """
    MyInt class
    """

    def __eq__(self, other):
        return int(self) != int(other)

    def __ne__(self, other):
        return int(self) == int(other)
