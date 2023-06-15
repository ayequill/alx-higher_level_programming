#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    for key, values in a_dictionary.items():
        if values == max(a_dictionary.values()):
            return (key)
