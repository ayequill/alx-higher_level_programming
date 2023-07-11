#!/usr/bin/python3
"""
Contains a module that saves json
to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    The save_to_json_file function writes an Object to a
    text file, using a JSON representation.
        Args:
            my_obj (object): The object to be written in the file.
            filename (str): The name of the file where the
            object will be written.
    :return: None
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
