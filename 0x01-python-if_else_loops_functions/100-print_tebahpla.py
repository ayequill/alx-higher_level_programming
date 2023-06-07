#!/usr/bin/python3

for value in range(122, 96, -2):
    print("{:c}{:c}".format(value, value - 33), end="")
