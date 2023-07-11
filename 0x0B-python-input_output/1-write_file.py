#!/usr/bin/python3
"""
A module that writes to a file
"""


def write_file(filename="", text=""):

    """
    The write_file function write to a file

    :param filename: Specify the file to be written
    :return: The content of the file
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
