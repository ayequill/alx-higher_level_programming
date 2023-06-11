#!/usr/bin/python3
"""  Prints a list of integers reversed   """


def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    rev = my_list.reverse()
    for number in rev:
        print("{:d}".format(number))
