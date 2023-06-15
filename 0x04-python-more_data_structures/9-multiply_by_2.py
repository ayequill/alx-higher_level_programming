#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return dict(map(lambda element:
                    (element[0], element[1] * 2), a_dictionary.items()))
