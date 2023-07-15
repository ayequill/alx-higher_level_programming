#!/usr/bin/python3
"""
Test Base class module
"""
import unittest
import json
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
    
        
    