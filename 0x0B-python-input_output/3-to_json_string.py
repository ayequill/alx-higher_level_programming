#!/usr/bin/python3
"""
This module contains a function that
that converts an object to json format
"""
import json


def to_json_string(my_obj):
    """
    The to_json_string function takes an object and returns
    a JSON representation of it.
    :param my_obj: Pass the object to be serialized
    :return: A string representing the object
    """
    return json.dumps(my_obj)
