#!/usr/bin/python3
"""  Prints a list of integers reversed   """


def print_reversed_list_integers(my_list=[]):
    rev = my_list[::-1]
    for number in rev:
        print("{}".format(number))
