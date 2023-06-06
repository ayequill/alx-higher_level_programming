#!/usr/bin/python3

def uppercase(str):
    new_str = ""
    for c in str:
        if(ord(c) >= ord('a') and ord(c) <= ord('z')):
            new_str += chr(ord(c) - 32)
            char = chr(ord(c) - 32)
        else:
            new_str += c
    print(new_str)