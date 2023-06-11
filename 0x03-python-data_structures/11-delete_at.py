#!/usr/bin/python3
""" Deletes an item at a specific position in the list """


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        my_list.remove(idx + 1)
    return my_list
