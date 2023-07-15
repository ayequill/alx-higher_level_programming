#!/usr/bin/python3
"""
Test Rectangle class module
"""
import unittest
import json
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rect1 = Rectangle(10, 2)
        self.rec_dict = {"id": 66,
                         "width": 10,
                         "height": 10,
                         "x": 10,
                         "y": 10}
        pass

    def tearDown(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(self.rect1.id, 1)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r2.id, 3)

    def test_has_attrib(self):
        self.assertTrue(hasattr(self.rect1, "width"))
        self.assertTrue(hasattr(self.rect1, "x"))
        self.assertTrue(hasattr(self.rect1, "id"))
        self.assertTrue(hasattr(self.rect1, "y"))
        self.assertTrue(hasattr(self.rect1, "height"))

    def test_rect_area(self):
        self.assertEqual(self.rect1.area(), 20)

    def test_string_as_arg(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(2, '10')
            rect.area(1)

    def test_negative_arg(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(-2, -10)

    def test_infinity_arg(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(float("inf"), float("inf"))

    def test_str_representation(self):
        rect2 = Rectangle(10, 10, 10, 42)
        self.assertEqual(str(rect2), '[Rectangle] (2) 10/42 - 10/10')

    def test_update(self):
        update = {"id": 66, "width": 10, "height": 10, "x": 10, "y": 10}
        rect = Rectangle(2, 2, 2, 2)
        rect.update(**update)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 10)
        self.assertEqual(rect.id, 66)
        self.assertEqual(rect.y, 10)

    
    def test_rect_display(self):
        r1 = Rectangle(6, 2, 0, 0)
        # self.as(r1.display(), "############")
        self.assertTrue(isinstance(r1.display().__str__(), str))
    
    def test_rect_to_dictionary(self):
        rect_dict = self.rect1.to_dictionary()
        self.assertIsInstance(rect_dict, dict)
        self.assertIn("id", rect_dict)
        self.assertIn("x", rect_dict)
        self.assertIn("width", rect_dict)
        self.assertIn("height", rect_dict)
        self.assertIn("y", rect_dict)
        self.assertEqual(len(rect_dict.keys()), 5)

    def test_create_instance(self):
        new_rect = Rectangle.create(**self.rec_dict)
        self.assertIsInstance(new_rect, Rectangle)
    
    def test_to_json_string(self):
        rect_dict = self.rect1.to_dictionary()
        json_str = self.rect1.to_json_string(rect_dict)
        self.assertIsInstance(json_str, str)
    
    def test_to_json_string_empty(self):
        self.assertEqual(Rectangle.to_json_string(None), '[]')
    
    def test_inheritance(self):
        self.assertTrue(issubclass(Rectangle, Base))
        
    def test_save_to_file(self):
        Rectangle.save_to_file(None)
        with open()