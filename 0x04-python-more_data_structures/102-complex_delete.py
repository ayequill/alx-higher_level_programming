#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    for key, item in dict(a_dictionary).items():
        if value == item:
            del a_dictionary[key]
    return a_dictionary
