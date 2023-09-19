#!/usr/bin/python3
""" 14. Square instance to dictionary representation """
import unittest
from models.square import Square


class TestSquareToDictionary(unittest.TestCase):

    def test_to_dictionary(self):
        s = Square(5, 2, 3, 1)

        result = s.to_dictionary()

        self.assertIsInstance(result, dict)

        self.assertIn('id', result)
        self.assertIn('size', result)
        self.assertIn('x', result)
        self.assertIn('y', result)

        self.assertEqual(result['id'], s.id)
        self.assertEqual(result['size'], s.size)
        self.assertEqual(result['x'], s.x)
        self.assertEqual(result['y'], s.y)


if __name__ == "__main__":
    unittest.main()
