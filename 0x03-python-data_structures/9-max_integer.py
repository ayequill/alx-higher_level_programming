#!/usr/bin/python3
""" Find the biggest integer in a list of integers """

def max_integer(my_list=[]):
    if len(my_list) != 0:
        sorted_numbers = my_list[:]
        sorted_numbers.sort()
        return sorted_numbers[-1]
