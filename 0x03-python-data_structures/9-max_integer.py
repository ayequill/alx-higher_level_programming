#!/usr/bin/python3
""" Find the biggest integer in a list of integers """

def max_integer(my_list=[]):
    sorted_numbers = my_list[:]
    sorted_numbers.sort()
    return sorted_numbers[-1]
