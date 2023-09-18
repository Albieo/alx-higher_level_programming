#!/usr/bin/python3
""" 4. Area first """
import unittest
from models.rectangle import Rectangle


class TestRectangleArea(unittest.TestCase):

    def test_area(self):
        r1 = Rectangle(5, 10)
        self.assertEqual(r1.area(), 50)

        r2 = Rectangle(3, 7)
        self.assertEqual(r2.area(), 21)

        r3 = Rectangle(0, 0)
        self.assertEqual(r3.area(), 0)

if __name__ == "__main__":
    unittest.main()
