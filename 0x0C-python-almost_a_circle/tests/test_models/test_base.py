#!/usr/bin/python3
"""
Test Base class module
"""
import unittest
import json
from os import path, remove
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    
    def setUp(self):
        # self.base1 = Base(1)
        # self.base2 = Base(19)
        # self.r1 = Rectangle(10, 7, 2, 8)
        # self.r2 = Rectangle(2, 4)
        # self.r1 = Rectangle(10, 7, 2, 8)
        # self.rec_dict = self.r1.to_dictionary()
        # self.s1 = Square(11, 2, 3, 3)
        pass
    def tearDown(self):
        Base._Base__nb_objects = 0
        paths = (
            'Rectangle.csv',
            'Rectangle.json',
            'Square.csv',
            'Square.json'
        )
        for path_ in paths:
            if path.exists(path_):
                remove(path_)
        
        
    def test_id_integer(self):
        b1 = Base()
        b2 = Base(5)
        b3 = Base(12)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 5)
        self.assertEqual(b3.id, 12)
    
    def test_id_float(self):
        b1 = Base(8.8)
        b2 = Base(float("inf"))
        self.assertEqual(b1.id, 8.8)
        self.assertEqual(b2.id, float("inf"))
        
    def test_id_string(self):
        b1 = Base("Hello")
        self.assertEqual(b1.id, "Hello")
    
    
    def test_has_attrib(self):
        base1 = Base(10)
        self.assertTrue(hasattr(base1,'_Base__nb_objects'), 0)
        self.assertTrue(hasattr(base1, 'id'), 0)
        self.assertTrue(hasattr(base1, 'load_from_file'), 0)
        self.assertTrue(hasattr(base1, 'to_json_string'), 0)
    
    def test_json_to_string_empty(self):
        base1 = Base(10)
        self.assertEqual(base1.to_json_string(None), '[]')
    
    def test_rectangle_to_dictionary(self):
        r1 = Rectangle(10, 7, 2, 8)
        s1 = Square(1, 1)
        rec_dict = r1.to_dictionary()
        # self.assertEqual(rec_dict, {'id': 2, 'width': 10, 'height': 7, 'x': 2, 'y': 8})
        self.assertIn('id', rec_dict)
        
    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)
    def test_two_args(self):
        with self.assertRaises(TypeError):
            b1 = Base(1, 2)

class TestBase_to_json_operation(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    def test_to_json_string_rectangle_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_type(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)
        
    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

    def test_create_instances(self):
        """ testing load_from_file class method """

        r = Rectangle(1, 2)
        self.assertIsInstance(r, Rectangle)
        Square.save_to_file([r])
        items = Square.load_from_file()
        self.assertIsInstance(items, list)
        for i in items:
            self.assertIsInstance(i, Square)

        r = Square(1, 2)
        self.assertIsInstance(r, Square)
        Rectangle.save_to_file([r])
        items = Rectangle.load_from_file()
        self.assertIsInstance(items, list)
        for i in items:
            self.assertIsInstance(i, Rectangle)
    
        
    