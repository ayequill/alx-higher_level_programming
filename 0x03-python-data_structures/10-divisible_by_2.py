#!/usr/bin/python3
"""finds all multiples of 2 in a list."""


def divisible_by_2(my_list=[]):
    return [True if number % 2 == 0 else False for number in my_list]
