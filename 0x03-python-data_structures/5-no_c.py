#!/usr/bin/python3
""" Removes an occurrence of c and C from a string. """


def no_c(my_string):
    return "".join(char for char in my_string if char not in "Cc")
