#!/usr/bin/python3
"""
Contains a modules that loads, saves
and adds to a file
"""
from sys import argv

if __name__ == "__main__":

    load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

    try:
        args = load_from_json_file("add_item.json")
    except FileNotFoundError:
        args = []
    args.extend(argv[1:])
    save_to_json_file(args, "add_item.json")
