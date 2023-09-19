#!/usr/bin/python3
""" 8. Update #0 """
import unittest
from models.rectangle import Rectangle


class TestRectangleUpdate1(unittest.TestCase):

    def test_update_with_args(self):
        r = Rectangle(5, 10, 2, 3, 1)

        r.update(2, 7, 12, 4, 6)

        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 6)

    def test_update_with_less_args(self):
        r = Rectangle(5, 10, 2, 3, 1)

        r.update(7, 12)

        self.assertEqual(r.id, 7)
        self.assertEqual(r.width, 12)

    def test_update_with_more_args(self):
        r = Rectangle(5, 10, 2, 3, 1)

        r.update(2, 7, 12, 4, 6, 8)

        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 6)


if __name__ == "__main__":
    unittest.main()
