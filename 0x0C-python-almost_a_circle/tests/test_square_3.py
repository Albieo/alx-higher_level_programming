#!/usr/bin/python3
""" 12. Square update """
import unittest
from models.square import Square


class TestSquareUpdateMethod(unittest.TestCase):

    def test_update_with_args(self):
        s = Square(5, 2, 3, 1)

        s.update(2, 7, 4, 6)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 6)

    def test_update_with_kwargs(self):
        s = Square(5, 2, 3, 1)

        s.update(size=8, y=7, x=4, id=2)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 7)

    def test_update_with_both_args_and_kwargs(self):
        s = Square(5, 2, 3, 1)

        s.update(2, 7, x=4, y=6)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_update_with_args_skipping_kwargs(self):
        s = Square(5, 2, 3, 1)

        s.update(2, 7)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_update_with_kwargs_skipping_args(self):
        s = Square(5, 2, 3, 1)

        s.update(x=4, y=6)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 6)


if __name__ == "__main__":
    unittest.main()
