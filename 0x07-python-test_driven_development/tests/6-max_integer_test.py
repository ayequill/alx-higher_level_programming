#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test case class for max_integer function"""

    def setUp(self):
        """Set up test data"""
        self.ord_li = max_integer([1, 2, 3, 4])
        self.unord_li = max_integer([4, 3, 2, 1])
        self.empty_li = max_integer([])
        self.str_li = max_integer(['car', 'book', 'and'])
        self.str = max_integer('siaw')
        self.empty_str = max_integer('')
        self.tuple_li = max_integer((1, 2, 3))
        self.max_in_mid = max_integer([1, 4, 2])
        self.one_element = max_integer([1])

    def test_ordered_list(self):
        """Test max_integer with an ordered list"""
        self.assertEqual(self.ord_li, 4)

    def test_unordered_list(self):
        """Test max_integer with an unordered list"""
        self.assertEqual(self.unord_li, 4)

    def test_empty_list(self):
        """Test max_integer with an empty list"""
        self.assertEqual(self.empty_li, None)

    def test_string_list(self):
        """Test max_integer with a list of strings"""
        self.assertEqual(self.str_li, 'car')

    def test_str(self):
        """Test max_integer with a string"""
        self.assertEqual(self.str, 'w')

    def test_empty_string(self):
        """Test max_integer with an empty string"""
        self.assertEqual(self.empty_str, None)

    def test_tuple(self):
        """Test max_integer with a tuple"""
        self.assertEqual(self.tuple_li, 3)

    def test_max_in_middlen(self):
        """
        Text max integer with max in middle
        """
        self.assertEqual(self.max_in_mid, 4)

    def test_one_integer(self):
        """
        Checking for only one element 
        """
        self.assertEqual(self.one_element, 1)


if __name__ == '__main__':
    unittest.main()
