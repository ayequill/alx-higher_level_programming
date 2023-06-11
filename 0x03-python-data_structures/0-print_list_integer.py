#!/usr/bin/python3
if __name__ == "__main__":
    """Prints all integers in a list"""
    def print_list_integer(my_list=[]):
        for item in my_list:
            print("{:d}".format(item))
