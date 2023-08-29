#!/usr/bin/python3
"""Define a class Square."""


class Square():
    """
    A class representing a square.

    Attributes:
        __size (int): The side length of the square.

    Methods:
        __init__(self, size=0):
            Initializes a new Square instance with the specified size.

    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance with the specified size.

        Args:
            size (int): The side length of the square.
                        Defaults to 0 if not provided.
        """
        self.__size = size
