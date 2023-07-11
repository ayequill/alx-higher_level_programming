#!/usr/bin/python3
"""
A module that contains a function that
that compares objects
"""


def is_same_class(obj, a_class):
    """
    returns a True if obj is of the same as or False
    """
    return type(obj) == a_class
