#!/usr/bin/python3
""" 8. Update #1 """
import unittest
from models.rectangle import Rectangle


class TestRectangleUpdate2(unittest.TestCase):

    def test_update_with_args(self):
        r = Rectangle(5, 10, 2, 3, 1)
        r.update(7, 8, 9, 10, 11)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 9)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 11)
        self.assertEqual(r.id, 7)

    def test_update_with_kwargs(self):
        r = Rectangle(5, 10, 2, 3, 1)
        r.update(width=7, height=8, x=9, y=10, id=11)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 9)
        self.assertEqual(r.y, 10)
        self.assertEqual(r.id, 11)


if __name__ == "__main__":
    unittest.main()
