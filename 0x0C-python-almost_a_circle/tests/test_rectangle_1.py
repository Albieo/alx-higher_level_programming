#!/usr/bin/python3
""" 2. First Rectangle """
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):

    def test_constructor(self):
        rect = Rectangle(5, 10)
        self.assertIsInstance(rect, Rectangle)
        self.assertIsInstance(rect, Base)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertIsNotNone(rect.id)

    def test_width_getter_setter(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.width, 5)
        rect.width = 15
        self.assertEqual(rect.width, 15)

    def test_height_getter_setter(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.height, 10)
        rect.height = 20
        self.assertEqual(rect.height, 20)

    def test_x_getter_setter(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.x, 0)
        rect.x = 25
        self.assertEqual(rect.x, 25)

    def test_y_getter_setter(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.y, 0)
        rect.y = 30
        self.assertEqual(rect.y, 30)


if __name__ == "__main__":
    unittest.main()
