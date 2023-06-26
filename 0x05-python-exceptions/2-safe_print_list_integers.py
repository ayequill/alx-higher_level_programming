#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    total_len_list: int = 0
    for item in range(x):
        try:
            print("{:d}".format(my_list[item]), end="")
            total_len_list += 1
        except (ValueError, TypeError):
            pass
    print()
    return total_len_list
