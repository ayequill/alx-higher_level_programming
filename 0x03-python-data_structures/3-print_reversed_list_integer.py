#!/usr/bin/python3
"""print_reversed_list_integer(my_list=[])
    Prints a list of integers reversed
"""


def print_reversed_list_integers(my_list=[]):
    rev = my_list[len(my_list)-1 : :- 1 ]
    for number in rev:
        print("{}".format(number))