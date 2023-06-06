#!/usr/bin/python3

def isLower(c):
    if(ord(c) >= ord('a') and ord(c) <= ord('z')):
        print("{:s} is lower".format(c))
    else:
        print("{:s} is upper".format(c))
