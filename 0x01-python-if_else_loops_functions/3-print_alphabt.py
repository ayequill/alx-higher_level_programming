#!/usr/bin/python3

for ascii_value in range(97, 123):
    if (chr(ascii_value) != 'p' and chr(ascii_value) != 'e'):
        print("{:s}".format(chr(ascii_value)), end="")
