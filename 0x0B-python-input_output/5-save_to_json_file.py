#!/usr/bin/python3
"""
Contains a module that saves json
to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    The save_to_json_file function writes an Object to a
    text file, using a JSON representation.
        Args:
            my_obj (object): The object to be written in the file.
            filename (str): The name of the file where the
            object will be written.
    :return: None
    """
    json_rep = json.dumps(my_obj)

    with open(filename, "w", encoding="utf-8") as file:
        file.write(json_rep)

filename = "my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)

filename = "my_dict.json"
my_dict = {
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
save_to_json_file(my_dict, filename)

try:
    filename = "my_set.json"
    my_set = { 132, 3 }
    save_to_json_file(my_set, filename)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
