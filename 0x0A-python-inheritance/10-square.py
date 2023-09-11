#!/usr/bin/python3
""" Square #1 """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square, which is a special case of
    a rectangle with equal sides.

    Attributes:
        __size (int): The size of each side of the square.
    """

    def __init__(self, size):
        """
        Initializes a new Square object with the given size.

        Args:
            size (int): The size of each side of the square.
        """
        super().__init__(size, size)
        self.__size = size
