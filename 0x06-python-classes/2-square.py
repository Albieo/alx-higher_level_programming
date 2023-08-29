#!/usr/bin/python3
"""Define a class Square."""


class Square():
    """
    A class representing a square.

    Attributes:
        __size (int): The size of the square's sides.

    Methods:
        __init__(self, size=0):
            Initializes a new square with the specified size.

            Args:
                size (int, optional): The size of the square's sides.
                                        Default is 0.

            Raises:
                TypeError: If size is not an integer.
                ValueError: If size is less than 0.
    """

    def __init__(self, size=0):
        """
        Initializes a new square with the specified size.

        Args:
            size (int, optional): The size of the square's sides. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
