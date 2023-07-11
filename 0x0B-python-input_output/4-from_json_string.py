#!/usr/bin/python3
"""
Contains a module that converts json
data to python objects
"""
import json


def from_json_string(my_str):
    """
    The from_json_string function takes a JSON string
    and returns an object (Python data structure)
    represented by the parameter.
    :param my_str: Pass a string to the function
    :return: An object represented by a json string
    """
    return json.loads(my_str)
