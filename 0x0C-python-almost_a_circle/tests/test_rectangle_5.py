#!/usr/bin/python3
""" 6. __str__ """
import unittest
from models.rectangle import Rectangle


class TestRectangleStrMethod(unittest.TestCase):

    def test_str_method(self):
        r = Rectangle(5, 10, 2, 3, 1)

        expected_str = "[Rectangle] (1) 2/3 - 5/10"
        self.assertEqual(str(r), expected_str)


if __name__ == "__main__":
    unittest.main()
