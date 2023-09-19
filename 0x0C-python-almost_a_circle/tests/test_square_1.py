#!/usr/bin/python3
""" 10. And now, the Square """
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_constructor(self):
        s = Square(5, 2, 3, 1)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 1)

    def test_getters_and_setters(self):
        s = Square(5, 2, 3, 1)

        s.size = 7
        self.assertEqual(s.width, 7)
        self.assertEqual(s.height, 7)

        s.x = 4
        self.assertEqual(s.x, 4)

        s.y = 6
        self.assertEqual(s.y, 6)

    def test_id_inherited(self):
        s = Square(5, 2, 3, 1)
        self.assertEqual(s.id, 1)

    def test_str_method(self):
        s = Square(5, 2, 3, 1)
        self.assertEqual(str(s), "[Square] (1) 2/3 - 5")


if __name__ == "__main__":
    unittest.main()
