#!/usr/bin/python3
"""
Test Rectangle class module
"""
import unittest
# from os import path
from os import path, remove
import json
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle
class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.square1 = Square(10)
        self.square_dict = {"id": 66,
                         "size": 10,
                         "x": 10,
                         "y": 10}
        pass

    def tearDown(self):
        Base._Base__nb_objects = 0
        if path.exists("Square.json"):
            remove("Square.json")
        

    def test_id(self):
        s1 = Square(10)
        s2 = Square(2)
        self.assertEqual(self.square1.id, 1)
        self.assertEqual(s1.id, 2)
        self.assertEqual(s2.id, 3)

    def test_has_attrib(self):
        self.assertTrue(hasattr(self.square1, "size"))
        self.assertTrue(hasattr(self.square1, "x"))
        self.assertTrue(hasattr(self.square1, "id"))
        self.assertTrue(hasattr(self.square1, "y"))

    def test_rect_area(self):
        self.assertEqual(self.square1.area(), 100)

    def test_string_as_arg(self):
        with self.assertRaises(TypeError):
            s1 = Square(2, '10')
            s1.area(1)

    def test_negative_arg(self):
        with self.assertRaises(ValueError):
            s1 = Square(-2)

    def test_infinity_arg(self):
        with self.assertRaises(TypeError):
            sq = Square(float("inf"))

    def test_str_representation(self):
        s1 = Square(10)
        self.assertEqual(str(s1), '[Square] (2) 0/0 - 10')

    def test_update(self):
        update = {"id": 66, "size": 10, "x": 10, "y": 10}
        s1 = Square(2)
        s1.update(**update)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.x, 10)
        self.assertEqual(s1.id, 66)
        self.assertEqual(s1.y, 10)

    
    # def test_rect_display(self):
    #     r1 = Rectangle(6, 2, 0, 0)
    #     # self.as(r1.display(), "############")
    #     self.assertTrue(isinstance(r1.display().__str__(), str))
    
    def test_rect_to_dictionary(self):
        s1_dict = self.square1.to_dictionary()
        self.assertIsInstance(s1_dict, dict)
        self.assertIn("id", s1_dict)
        self.assertIn("x", s1_dict)
        self.assertIn("size", s1_dict)
        self.assertIn("y", s1_dict)
        self.assertEqual(len(s1_dict.keys()), 4)

    def test_create_instance(self):
        new_square = Square.create(**self.square_dict)
        self.assertIsInstance(new_square, Square)
    
    def test_to_json_string(self):
        s1_dict = self.square1.to_dictionary()
        json_str = self.square1.to_json_string(s1_dict)
        self.assertIsInstance(json_str, str)
    
    def test_to_json_string_empty(self):
        self.assertEqual(Square.to_json_string(None), '[]')
    
    def test_inheritance(self):
        self.assertTrue(issubclass(Square, Base))
        self.assertTrue(issubclass(Square, Rectangle))
        
    def test_save_to_file(self):
        s1_save = Square(10)
        Square.save_to_file([self.square1, s1_save])
        with open('Square.json', 'r') as f:
            self.assertIn('id', f.read())
    
    def test_save_empty_to_file(self):
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertIn('[]', f.read())
    
    def test_load_from_file(self):
        s1 = Rectangle(2, 10)
        Square.save_to_file([self.square1, s1])
        instances = Square.load_from_file()
        for i in range(len(instances)):
            self.assertEqual(instances[i].id, i + 1)
            self.assertIsInstance(instances[i], Square)
    
    # # def test_create_rectangle(self):
        