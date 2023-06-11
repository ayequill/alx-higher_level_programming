#!/usr/bin/python3
"""print_reversed_list_integer(mylist=[])
    Prints a list of integers reversed
"""


def print_reversed_list_integers(mylist=[]):
    rev = mylist[::-1]
    for number in rev:
        print("{}".format(number))
