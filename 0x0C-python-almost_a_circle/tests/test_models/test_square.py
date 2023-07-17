#!/usr/bin/python3
"""
Test Rectangle class module
"""
import unittest
from os import path, remove
from sys import stdout, __stdout__
from io import StringIO
import json
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Testcases for the rectangle class

    Args:
        unittest (TestCase): 
    """

    def setUp(self):
        """
        Set up the test fixture.
        """
        self.square1 = Square(10)
        self.square_dict = {"id": 66,
                            "size": 10,
                            "x": 10,
                            "y": 10}
        pass

    def tearDown(self):
        """
        Clean up after the test.
        """
        Base._Base__nb_objects = 0
        if path.exists("Square.json"):
            remove("Square.json")
        stdout = __stdout__

    def test_id(self):
        """
        Test the assignment of unique IDs to Rectangle instances.
        """
        s1 = Square(10)
        s2 = Square(2)
        self.assertEqual(self.square1.id, 1)
        self.assertEqual(s1.id, 2)
        self.assertEqual(s2.id, 3)

    def test_has_attrib(self):
        """
        Test if Square instances have the required attributes.
        """
        self.assertTrue(hasattr(self.square1, "size"))
        self.assertTrue(hasattr(self.square1, "x"))
        self.assertTrue(hasattr(self.square1, "id"))
        self.assertTrue(hasattr(self.square1, "y"))

    def test_rect_area(self):
        """
        Test the calculation of the area of a Square.
        """
        self.assertEqual(self.square1.area(), 100)

    def test_string_as_arg(self):
        """
        Test the behavior when passing a string as an argument to Square.
        """
        with self.assertRaises(TypeError):
            s1 = Square(2, '10')
            s1.area(1)

    def test_negative_arg(self):
        """
        Test the behavior when passing a negative argument to Square.
        """
        with self.assertRaises(ValueError):
            s1 = Square(-2)

    def test_infinity_arg(self):
        """
        Test the behavior when passing infinity as an argument to Square.
        """
        with self.assertRaises(TypeError):
            sq = Square(float("inf"))

    def test_str_representation(self):
        """
        Test the string representation of a Square.
        """
        s1 = Square(10)
        self.assertEqual(str(s1), '[Square] (2) 0/0 - 10')

    def test_update(self):
        """
        Test the update method of the Square class.
        """
        update = {"id": 66, "size": 10, "x": 10, "y": 10}
        s1 = Square(2)
        s1.update(**update)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.x, 10)
        self.assertEqual(s1.id, 66)
        self.assertEqual(s1.y, 10)

    # def test_rect_display(self):
    #     s1 = Square(2)
    #     output = StringIO()
    #     stdout = output
    #     # self.assertTrue(isinstance(r1.display().__str__(), str))
    #     print_statement = output.getvalue()
    #     print(print_statement)

    def test_rect_to_dictionary(self):
        """
        Test the conversion of a Square instance to a dictionary.
        """
        s1_dict = self.square1.to_dictionary()
        self.assertIsInstance(s1_dict, dict)
        self.assertIn("id", s1_dict)
        self.assertIn("x", s1_dict)
        self.assertIn("size", s1_dict)
        self.assertIn("y", s1_dict)
        self.assertEqual(len(s1_dict.keys()), 4)

    def test_create_instance(self):
        """
        Test creating a Square instance from a dictionary.
        """
        new_square = Square.create(**self.square_dict)
        self.assertIsInstance(new_square, Square)

    def test_to_json_string(self):
        """
        Test converting a dictionary to a JSON string.
        """
        s1_dict = self.square1.to_dictionary()
        json_str = self.square1.to_json_string(s1_dict)
        self.assertIsInstance(json_str, str)

    def test_to_json_string_empty(self):
        """
        Test converting an empty list to a JSON string.
        """
        self.assertEqual(Square.to_json_string(None), '[]')

    def test_inheritance(self):
        """
        Test the inheritance of the Square class.
        """
        self.assertTrue(issubclass(Square, Base))
        self.assertTrue(issubclass(Square, Rectangle))

    def test_save_to_file(self):
        """
        Test saving Square instances to a JSON file.
        """
        s1_save = Square(10)
        Square.save_to_file([self.square1, s1_save])
        with open('Square.json', 'r') as f:
            self.assertIn('id', f.read())

    def test_save_empty_to_file(self):
        """
        Test saving an empty list to a JSON file.
        """
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertIn('[]', f.read())

    def test_load_from_file(self):
        """
        Test loading Square instances from a JSON file.
        """
        s1 = Rectangle(2, 10)
        Square.save_to_file([self.square1, s1])
        instances = Square.load_from_file()
        for i in range(len(instances)):
            self.assertEqual(instances[i].id, i + 1)
            self.assertIsInstance(instances[i], Square)

    def test_save_to_csv(self):
        """
        Test saving Square instances to a CSV file.
        """
        square_save = Rectangle(2, 10)
        Square.save_to_file([self.rect1, rect_save])
        instances = Rectangle.load_from_file_csv()
        for instance in instances:
            self.assertIsInstance(instance, Rectangle)

    def test_save_to_csv_empty(self):
        """
        Test saving an empty list to a CSV file.
        """
        Rectangle.save_to_file_csv([])
        output = Rectangle.load_from_file_csv()
        self.assertEqual(output, [])
