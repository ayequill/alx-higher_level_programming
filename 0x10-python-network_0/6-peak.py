#!/usr/bin/python3
""" This module find the peak of an unsorted list """


def find_peak(list_of_integers):
    """ Finds the peak element """
    if not list_of_integers or len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]

    if len(list_of_integers) == 2:
        return max(list_of_integers)

    left = 0
    right = len(list_of_integers) - 1

    while left <= right:
        mid = (left + right) // 2

        # Here i check if mid is the first element in the list
        # or the last in the list.
        # If it is i just need one condition to be true because i only
        # need to check one neighbor,
        # Then i check its neighbors.
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1])\
            and (mid == len(list_of_integers) - 1
                 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        # Check if the loop is still running and check if the pivot is lesser
        # than its
        # left neighbor, if true we move left
        elif mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            right = mid - 1
        # If not we move right
        else:
            left = mid + 1
