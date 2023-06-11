#!/usr/bin/python3
"""  Prints a list of integers reversed   """


def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    else:
        for number in reversed(my_list):
            print("{:d}".format(number))
