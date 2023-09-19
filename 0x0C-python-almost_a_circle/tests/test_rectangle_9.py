#!/usr/bin/python3
""" 13. Rectangle instance to dictionary representation """
import unittest
from models.rectangle import Rectangle


class TestRectangleToDictionary(unittest.TestCase):

    def test_to_dictionary(self):
        r = Rectangle(5, 10, 2, 3, 1)

        result = r.to_dictionary()

        self.assertIsInstance(result, dict)

        self.assertIn('id', result)
        self.assertIn('width', result)
        self.assertIn('height', result)
        self.assertIn('x', result)
        self.assertIn('y', result)

        self.assertEqual(result['id'], r.id)
        self.assertEqual(result['width'], r.width)
        self.assertEqual(result['height'], r.height)
        self.assertEqual(result['x'], r.x)
        self.assertEqual(result['y'], r.y)


if __name__ == "__main__":
    unittest.main()
