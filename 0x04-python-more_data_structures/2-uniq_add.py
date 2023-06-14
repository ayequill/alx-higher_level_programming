#!/usr/bin/python3

def uniq_add(my_list=[]):
    return sum(list(map(lambda number: number, set(my_list))))
