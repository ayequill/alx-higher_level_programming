#!/usr/bin/python3
"""
Base class
"""
import json


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the base class
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(json_str):
        """
        Returns json format of object
        Args:
            json_str (list): list
        Returns:
            dict: dict
        """
        if not json_str:
            return '[]'

        return json.dumps(json_str)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Serializes an object to json file
        Args:
            list_objs (list): list of instances
        """
        file_name = cls.__name__ + ".json"
        json_str = cls.to_json_string([x.to_dictionary() for x in list_objs])

        with open(file_name, "w", encoding="utf-8") \
                as out_file:
            out_file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Deserializes a json string to an object

        Args:
            json_string (list): _description_

        Returns:
            list: list of attribs
        """
        if not json_string or len(json_string) <= 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a new instances

        Returns:
            class: an instance of rectangle or square
        """
        name = cls.__name__

        if name == "Rectangle":
            new_rectangle = cls(1, 2)
            new_rectangle.update(**dictionary)
            return new_rectangle
        if name == "Square":
            new_rectangle = cls(1)
            new_rectangle.update(**dictionary)
            return new_rectangle

    @classmethod
    def load_from_file(cls):
        """
        Loads json from and returns a list of instances
        Returns:
            list: list of instances
        """
        name = cls.__name__
        file_name = name + ".json"
        instance_li = []
        try:
            with open(file_name, encoding="utf-8") \
                    as input_file:
                instances = cls.from_json_string(input_file.read())
        except FileNotFoundError:
            return []
        for instance in instances:
            instance_li.append(cls.create(**instance))
        return instance_li
