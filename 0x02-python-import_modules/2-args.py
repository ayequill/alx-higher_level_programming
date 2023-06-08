#!/usr/bin/python3

if __name__ == '__main__':
    """Prints the command line arguments"""
    from sys import argv

    num_of_args = len(argv) - 1

    if num_of_args == 0:
        print("0 arguments.")
    elif num_of_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_of_args))

    for arg in range(num_of_args):
        print("{}: {}".format(arg + 1, argv[arg + 1]))
