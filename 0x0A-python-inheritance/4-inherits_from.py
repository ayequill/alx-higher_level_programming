#!/usr/bin/python3
"""
A module that contains a  function that
returns True if the object is an instance
of a class
"""


def inherits_from(obj, a_class):
    """
    Method returns True if obj is inherited
    directly from a_class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
