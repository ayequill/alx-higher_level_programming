#!/usr/bin/python3
"""
Base class
"""
import json
from csv import writer, reader


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
            if list_objs is None or list_objs == []:
                out_file.write("[]")
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Saves a list of objects to a file
        with the class name preceded

        Args:
            list_objs (list): list of instances
        """
        file_name = cls.__name__ + ".csv"

        list_obj_dict = list(map(lambda obj: obj.to_dictionary(), list_objs))

        with open(file_name, mode="w", encoding="utf-8") as file:
            if list_objs is None or list_objs == []:
                file.write('[]')
            csv_file = writer(file)

            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    csv_file.writerow([
                        obj.id,
                        obj.width,
                        obj.height,
                        obj.x,
                        obj.y
                    ])

                if cls.__name__ == "Square":
                    csv_file.writerow([
                        obj.id,
                        obj.size,
                        obj.x,
                        obj.y
                    ])

    @classmethod
    def load_from_file_csv(cls):
        """
        Loads CSV from and returns a list of instances
        Returns:
            list: list of instances
        """
        file_name = cls.__name__ + ".csv"
        instance_list = []

        try:
            with open(file_name, encoding="utf-8", newline="") as file:
                csv_reader = reader(file)
                for row in csv_reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls(int(row[1]), int(row[2]), int(
                            row[3]), int(row[4]), int(row[0]))
                    elif cls.__name__ == "Square":
                        instance = cls(int(row[1]), int(
                            row[2]), int(row[3]), int(row[0]))
                    instance_list.append(instance)
        except (FileNotFoundError, IndexError):
            return []

        return instance_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all the Rectangles
        and Squares using Turtle graphics

        Args:
            list_rectangles (list): List of Rectangle instances
            list_squares (list): List of Square instances
        """
        import turtle

        screen = turtle.Screen()
        screen.bgcolor("white")

        for rect in list_rectangles:
            draw_rectangle(rect)

        for square in list_squares:
            draw_square(square)

        turtle.done()

    @staticmethod
    def draw_rectangle(rectangle):
        """
        Draws a rectangle using Turtle graphics

        Args:
            rectangle (Rectangle): Rectangle instance to draw
        """
        import turtle

        turtle.penup()
        turtle.goto(rectangle.x, rectangle.y)
        turtle.pendown()
        turtle.color("red")
        turtle.begin_fill()

        for _ in range(2):
            turtle.forward(rectangle.width)
            turtle.right(90)
            turtle.forward(rectangle.height)
            turtle.right(90)

        turtle.end_fill()

    @staticmethod
    def draw_square(square):
        """
        Draws a square using Turtle graphics

        Args:
            square (Square): Square instance to draw
        """
        import turtle

        turtle.penup()
        turtle.goto(square.x, square.y)
        turtle.pendown()
        turtle.color("blue")
        turtle.begin_fill()

        for _ in range(4):
            turtle.forward(square.size)
            turtle.right(90)

        turtle.end_fill()
