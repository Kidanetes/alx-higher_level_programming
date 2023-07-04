#!/usr/bin/python3
"""unittest for maximum integer from the list"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """test class for maximum integer of a list"""

    def test_max_at_end(self):
        """when a maximum integer is at the end"""
        a = [25, 53, 67]
        self.assertEqual(max_integer(a),67)

    def test_max_at_start(self):
        """when a maximum integer is at the beginning"""
        a = [78, 53, 43]
        self.assertEqual(max_integer(a), 78)

    def test_max_at_middle(self):
        """when a maximum integer is at the middle"""
        a = [25, 156, 67]
        self.assertEqual(max_integer(a), 156)

    def test_one_negative_number(self):
        """one negative number in a list"""
        a = [34, -67, 78, 99]
        self.assertEqual(max_integer(a), 99)

    def test_all_negative_number(self):
        """one negative number in a list"""
        a = [-34, -67, -78, -99]
        self.assertEqual(max_integer(a), -34)

    def test_one_number(self):
        """one negative number in a list"""
        a = [34]
        self.assertEqual(max_integer(a), 34)

    def test_empty_list(self):
        """one negative number in a list"""
        a = []
        self.assertEqual(max_integer(a), None)
    def test_floats(self):
        """Test a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """Test a string."""
        string = "Kidanemaryam"
        self.assertEqual(max_integer(string), 'y')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["hello", "hi"]
        self.assertEqual(max_integer(strings), "hi")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)
if __name__ == '__main__':
    unittest.main()
