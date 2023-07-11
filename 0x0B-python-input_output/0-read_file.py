#!/usr/bin/python3
"""
A module that prints the contents of a file
"""


def read_file(filename=""):

    """
    The read_file function reads a file and prints it to stdout.

    :param filename: Specify the file to be read
    :return: The content of the file
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
