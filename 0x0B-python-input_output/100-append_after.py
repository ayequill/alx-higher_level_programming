#!/usr/bin/python3
"""
Module that contains a function that
search and updates a file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    The append_after function inserts a new line
    of text to a file, after each line containing
    a specific string.


    :param filename: Specify the file to be opened
    :param search_string: Find the line in which we want to add
    :param new_string: Add the new string to the file
    """
    # TODO Refactor
    updated_str = ""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            updated_str += line
            if search_string in line:
                updated_str += new_string

    with open(filename, "w", encoding="utf-8") as file:
        file.write(updated_str)
