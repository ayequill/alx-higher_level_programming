#!/usr/bin/python3
"""
Module that contains a function that
loads json data from a file
"""


def class_to_json(obj):
    """
    The class_to_json function takes an object and returns a dictionary representation of the object.
    The function is used to convert objects into JSON format.

    :param obj: Pass in an instance of the class
    :return: A dictionary representation of an object
    """
    return obj.__dict__
