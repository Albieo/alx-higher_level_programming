#!/usr/bin/python3
""" 1. Base class """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_constructor_with_id(self):
        obj = Base(10)
        self.assertEqual(obj.id, 10)

    def test_constructor_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_constructor_with_negative_id(self):
        obj = Base(-5)
        self.assertEqual(obj.id, -5)

    def test_constructor_with_zero_id(self):
        obj = Base(0)
        self.assertEqual(obj.id, 0)


if __name__ == '__main__':
    unittest.main()
