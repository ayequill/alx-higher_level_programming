#!/usr/bin/python3
"""
A module that appends content to a file
"""


def append_write(filename="", text=""):
    """
    The append_write function appends a string to the end of a text file and returns
    the number of characters added.


    :param filename: Specify the file to be opened
    :param text: Write the text to the file
    :return: The number of characters added
    :doc-author: Trelent
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
