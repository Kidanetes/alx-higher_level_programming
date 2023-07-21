#!/usr/bin/python3
"""Unittest rectangle
Test cases for the Rectangle class
"""

import unittest
import io
import contextlib
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_2(self):
        """Test Rectangle class"""

        r0 = Rectangle(3, 4)
        self.assertEqual(r0.id, 1)
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.id, 2)
        r2 = Rectangle(8, 3)
        self.assertEqual(r2.id, 3)
        r3 = Rectangle(1, 4, 0, 0, 5)
        self.assertEqual(r3.id, 5)
        r4 = Rectangle(1, 4, 1, 3, 23)
        self.assertEqual(r4.id, 23)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r4.width, 1)
        self.assertEqual(r4.height, 4)
        self.assertEqual(r4.x, 1)
        self.assertEqual(r4.y, 3)
        with self.assertRaises(TypeError) as x:
            r0 = Rectangle(5)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'", str(
                x.exception))
        s = ("__init__() missing 2 required positional" +
             " arguments: 'width' and 'height'")
        with self.assertRaises(TypeError) as x:
            r1 = Rectangle()
        self.assertEqual(s, str(x.exception))
        self.assertTrue(isinstance(r1, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(isinstance(Rectangle, Base))

    def test_3(self):
        """Test Rectangle class"""

        with self.assertRaises(TypeError) as x:
            r = Rectangle("Hi", 5)
        self.assertEqual("width must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle(2, "hi")
        self.assertEqual("height must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle(1, 2, "hi", 3)
        self.assertEqual("x must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle(1, 2, 2, "hi")
        self.assertEqual("y must be an integer", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(0, 3)
        self.assertEqual("width must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(3, 0)
        self.assertEqual("height must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(6, -8)
        self.assertEqual("height must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(5, 6, -8, 9)
        self.assertEqual("x must be >= 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(5, 6, 8, -9)
        self.assertEqual("y must be >= 0", str(x.exception))

    def test_4(self):
        """Test for Rectangle class"""
        r1 = Rectangle(4, 3)
        self.assertEqual(r1.area(), 12)
        r2 = Rectangle(34, 3)
        self.assertEqual(r2.area(), 102)
        r3 = Rectangle(6, 3, 0, 0, 56)
        self.assertEqual(r3.area(), 18)
        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(3, 2)
            r1.area("Hello")
        self.assertEqual(
            "area() takes 1 positional argument but 2 were given", str(
                x.exception))

    def test_5(self):
        """Test for public method display."""

        f = io.StringIO()
        r1 = Rectangle(4, 5)
        with contextlib.redirect_stdout(f):
            r1.display()
        s = f.getvalue()
        res = "####\n####\n####\n####\n####\n"
        self.assertEqual(s, res)
        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(9, 6)
            r1.display(9)
        self.assertEqual(
            "display() takes 1 positional argument but 2 were given", str(
                x.exception))

    def test_6(self):
        """Test for __str__ representation."""

        f = io.StringIO()
        r1 = Rectangle(4, 6, 2, 1, 12)
        with contextlib.redirect_stdout(f):
            print(r1)
        s = f.getvalue()
        res = "[Rectangle] (12) 2/1 - 4/6\n"
        self.assertEqual(s, res)

    def test_7(self):
        """Test for public method display with x and y."""

        f = io.StringIO()
        r1 = Rectangle(2, 3, 2, 2)
        with contextlib.redirect_stdout(f):
            r1.display()
        s = f.getvalue()
        res = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(s, res)

    def test_8(self):
        """Test for public method update."""

        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)
        r1.update(89, 2)
        self.assertEqual(r1.width, 2)
        r1.update(89, 2, 3)
        self.assertEqual(r1.height, 3)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.x, 4)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)
        r1.update()
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError) as x:
            r1.update(65, 89, "hi")
        self.assertEqual("height must be an integer", str(x.exception))

    def test_9(self):
        """Test for public method update with kwargs."""

        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(r1.height, 1)
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.height, 2)
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError) as x:
            r1.update(height=65, x=2, width="hi")
        self.assertEqual("width must be an integer", str(x.exception))

    def test_13(self):
        """Test for public method to_dictionary."""

        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        r_dictionary = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(len(r1_dictionary), len(r_dictionary))
        self.assertEqual(type(r1_dictionary), dict)
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        r2_dictionary = r2.to_dictionary()
        self.assertEqual(len(r1_dictionary), len(r2_dictionary))
        self.assertEqual(type(r2_dictionary), dict)
        self.assertFalse(r1 == r2)
        s = "to_dictionary() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(10, 2, 1, 9)
            r1_dictionary = r1.to_dictionary("Hi")
        self.assertEqual(s, str(x.exception))


if __name__ == '__main__':
    unittest.main()
