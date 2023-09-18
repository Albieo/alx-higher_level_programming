#!/usr/bin/python3
""" 3. Validate attributes """
import unittest
from models.rectangle import Rectangle


class TestRectangleValidation(unittest.TestCase):

    def test_constructor_valid_inputs(self):
        r = Rectangle(5, 10, 2, 3)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

    def test_constructor_invalid_width(self):
        with self.assertRaises(ValueError) as context:
            r = Rectangle(0, 10, 2, 3)
            r.width = 0
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_constructor_invalid_height(self):
        with self.assertRaises(ValueError) as context:
            r = Rectangle(5, -10, 2, 3)
            r.height = -10
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_constructor_invalid_x(self):
        with self.assertRaises(ValueError) as context:
            r = Rectangle(5, 10, -2, 3)
            r.x = -2
        self.assertEqual(str(context.exception), "x must be >= 0")

    def test_constructor_invalid_y(self):
        with self.assertRaises(ValueError) as context:
            r = Rectangle(5, 10, 2, -3)
            r.y = -3
        self.assertEqual(str(context.exception), "y must be >= 0")

    def test_setter_width_valid(self):
        r = Rectangle(5, 10, 2, 3)
        r.width = 7
        self.assertEqual(r.width, 7)

    def test_setter_width_invalid(self):
        r = Rectangle(5, 10, 2, 3)
        with self.assertRaises(ValueError) as context:
            r.width = -7
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_setter_height_valid(self):
        r = Rectangle(5, 10, 2, 3)
        r.height = 12
        self.assertEqual(r.height, 12)

    def test_setter_height_invalid(self):
        r = Rectangle(5, 10, 2, 3)
        with self.assertRaises(ValueError) as context:
            r.height = 0
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_setter_x_valid(self):
        r = Rectangle(5, 10, 2, 3)
        r.x = 4
        self.assertEqual(r.x, 4)

    def test_setter_x_invalid(self):
        r = Rectangle(5, 10, 2, 3)
        with self.assertRaises(ValueError) as context:
            r.x = -4
        self.assertEqual(str(context.exception), "x must be >= 0")

    def test_setter_y_valid(self):
        r = Rectangle(5, 10, 2, 3)
        r.y = 6
        self.assertEqual(r.y, 6)

    def test_setter_y_invalid(self):
        r = Rectangle(5, 10, 2, 3)
        with self.assertRaises(ValueError) as context:
            r.y = -6
        self.assertEqual(str(context.exception), "y must be >= 0")

if __name__ == "__main__":
    unittest.main()
