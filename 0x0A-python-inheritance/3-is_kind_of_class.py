#!/usr/bin/python3
"""
A module that contains a function that
that compares objects
"""


def is_kind_of_class(obj, a_class):
    """
    returns True if an object is an instance of a_class
    or not
    """
    return isinstance(obj, a_class)
