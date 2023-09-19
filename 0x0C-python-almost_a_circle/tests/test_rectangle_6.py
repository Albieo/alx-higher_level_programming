#!/usr/bin/python3
""" 7. Display #1"""
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

    def test_display_r1(self):
        r1 = Rectangle(2, 3, 2, 2)
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        r1.display()
        self.assertEqual(self.stdout.getvalue(), expected_output)

    def test_display_r2(self):
        r2 = Rectangle(3, 2, 1, 0)
        expected_output = " ###\n ###\n"
        r2.display()
        self.assertEqual(self.stdout.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
