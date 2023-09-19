#!/usr/bin/python3
""" 11. Square size """
import unittest
from models.square import Square


class TestSquareGettersAndSetters(unittest.TestCase):

    def test_size_getter(self):
        s = Square(5, 2, 3, 1)
        self.assertEqual(s.size, 5)

    def test_size_setter_valid(self):
        s = Square(5, 2, 3, 1)
        s.size = 7
        self.assertEqual(s.size, 7)
        self.assertEqual(s.width, 7)
        self.assertEqual(s.height, 7)

    def test_size_setter_invalid_negative(self):
        s = Square(5, 2, 3, 1)
        with self.assertRaises(ValueError) as context:
            s.size = -7
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_size_setter_invalid_zero(self):
        s = Square(5, 2, 3, 1)
        with self.assertRaises(ValueError) as context:
            s.size = 0
        self.assertEqual(str(context.exception), "width must be > 0")


if __name__ == "__main__":
    unittest.main()
