#!/usr/bin/python3
""" 5. Display #0 """
import unittest
from models.rectangle import Rectangle
import io
import sys


class TestRectangleDisplay(unittest.TestCase):

    def setUp(self):
        self.stdout = io.StringIO()
        sys.stdout = self.stdout

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_display(self):
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        r.display()
        self.assertEqual(self.stdout.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
