#!/usr/bin/python3
"""
This module contains a function that idents sentences
"""


def text_indentation(text):
    """
    Idents a sentence with spaces

    Args:
        text (string): the text to indent
    Raises: TypeError if text is not a string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text_split = list(text)

    for i in range(len(text_split)):
        print(text_split[i], end="")
        if text_split[i] in ('.', ':', '?'):
            if i + 1 < len(text_split) and text_split[i + 1] == ' ':
                text_split[i + 1] = ''
            print("\n")
