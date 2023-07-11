#!/usr/bin/python3
"""
Module that contains a function that
loads json data from a file
"""
import json


def load_from_json_file(filename):
    """
    The load_from_json_file function creates an object from the JSON file.

    :param filename: Specify the file that will be loaded
    :return: An object (python data structure)
    """
    with open(filename) as file:
        return json.load(file)
