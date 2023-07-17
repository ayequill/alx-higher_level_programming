#!/usr/bin/python3
"""
Test Rectangle class module
"""
import unittest
from os import path, remove
import json
from csv import reader
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """
    Testcases for the Rectangle

    Args:
        unittest (_type_): _description_
    """

    def setUp(self):
        """
        Set up the test fixture.
        """
        self.rect1 = Rectangle(10, 2)
        self.rec_dict = {"id": 66,
                         "width": 10,
                         "height": 10,
                         "x": 10,
                         "y": 10}
        pass

    def tearDown(self):
        """
        Clean up after the test.
        """
        Base._Base__nb_objects = 0
        if path.exists("Rectangle.json"):
            remove("Rectangle.json")
        # if path.exists("Rectangle.csv"):
        #     remove("Rectangle.csv")

    def test_id(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(self.rect1.id, 1)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r2.id, 3)

    def test_has_attrib(self):
        """
        Test if Rectangle instances have the required attributes.
        """
        self.assertTrue(hasattr(self.rect1, "width"))
        self.assertTrue(hasattr(self.rect1, "x"))
        self.assertTrue(hasattr(self.rect1, "id"))
        self.assertTrue(hasattr(self.rect1, "y"))
        self.assertTrue(hasattr(self.rect1, "height"))

    def test_rect_area(self):
        """
        Test the calculation of the area of a Rectangle.
        """
        self.assertEqual(self.rect1.area(), 20)

    def test_string_as_arg(self):
        """
        Test the behavior when passing a string as an argument to Rectangle.
        """
        with self.assertRaises(TypeError):
            rect = Rectangle(2, '10')
            rect.area(1)

    def test_negative_arg(self):
        """
        Test the behavior when passing a negative argument to Rectangle.
        """
        with self.assertRaises(ValueError):
            rect = Rectangle(-2, -10)

    def test_infinity_arg(self):
        """
        Test the behavior when passing infinity as an argument to Rectangle.
        """
        with self.assertRaises(TypeError):
            rect = Rectangle(float("inf"), float("inf"))

    def test_str_representation(self):
        """
        Test the string representation of a Rectangle.
        """
        rect2 = Rectangle(10, 10, 10, 42)
        self.assertEqual(str(rect2), '[Rectangle] (2) 10/42 - 10/10')

    def test_update(self):
        """
        Test the update method of the Rectangle class.
        """
        update = {"id": 66, "width": 10, "height": 10, "x": 10, "y": 10}
        rect = Rectangle(2, 2, 2, 2)
        rect.update(**update)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 10)
        self.assertEqual(rect.id, 66)
        self.assertEqual(rect.y, 10)

    # def test_rect_display(self):
    #     r1 = Rectangle(6, 2, 0, 0)
    #     # self.as(r1.display(), "############")
    #     self.assertTrue(isinstance(r1.display().__str__(), str))

    def test_rect_to_dictionary(self):
        """
        Test the conversion of a Rectangle instance to a dictionary.
        """
        rect_dict = self.rect1.to_dictionary()
        self.assertIsInstance(rect_dict, dict)
        self.assertIn("id", rect_dict)
        self.assertIn("x", rect_dict)
        self.assertIn("width", rect_dict)
        self.assertIn("height", rect_dict)
        self.assertIn("y", rect_dict)
        self.assertEqual(len(rect_dict.keys()), 5)

    def test_create_instance(self):
        """
        Test creating a Rectangle instance from a dictionary.
        """
        new_rect = Rectangle.create(**self.rec_dict)
        self.assertIsInstance(new_rect, Rectangle)

    def test_to_json_string(self):
        """
        Test converting a dictionary to a JSON string.
        """
        rect_dict = self.rect1.to_dictionary()
        json_str = self.rect1.to_json_string(rect_dict)
        self.assertIsInstance(json_str, str)

    def test_to_json_string_empty(self):
        """
        Test converting an empty list to a JSON string.
        """
        self.assertEqual(Rectangle.to_json_string(None), '[]')

    def test_inheritance(self):
        """
        Test the inheritance of the Rectangle class.
        """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_save_to_file(self):
        """
        Test saving Rectangle instances to a JSON file.
        """
        rect_save = Rectangle(2, 10)
        Rectangle.save_to_file([self.rect1, rect_save])
        with open('Rectangle.json', 'r') as f:
            self.assertIn('id', f.read())

    def test_save_empty_to_file(self):
        """
        Test saving an empty list to a JSON file.
        """
        Rectangle.save_to_file([])
        with open("Rectangle.json") as f:
            self.assertIn('[]', f.read())

    def test_load_from_file(self):
        """
        Test loading Rectangle instances from a JSON file.
        """
        rect_save = Rectangle(2, 10)
        Rectangle.save_to_file([self.rect1, rect_save])
        ins = Rectangle.load_from_file()
        for i in range(len(ins)):
            self.assertEqual(ins[i].id, i + 1)
            self.assertIsInstance(ins[i], Rectangle)

    def test_save_to_csv(self):
        """
        Test saving Rectangle instances to a CSV file.
        """
        rect_save = Rectangle(2, 10)
        Rectangle.save_to_file([self.rect1, rect_save])
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
