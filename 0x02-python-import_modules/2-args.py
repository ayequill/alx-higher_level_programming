#!/usr/bin/python3

if __name__ == '__main__':
    """Prints the command line arguments"""
    from sys import argv

    num_of_cmd = len(argv) - 1

    if num_of_cmd == 0:
        print("0 arguments.")
    elif num_of_cmd == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_of_cmd))

    for cmd in range(num_of_cmd):
        print("{}: {}".format(cmd + 1, argv[cmd + 1]))
