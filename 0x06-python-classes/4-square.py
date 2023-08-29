#!/usr/bin/python3
"""Define a class Square."""


class Square():
    """
    A class representing a square.

    Attributes:
        __size (int): The size of the square's sides.

    Methods:
        __init__(self, size=0):
            Initializes a new Square object with a specified size.

            Args:
                size (int, optional): The size of the square's sides (default is 0).

        area(self):
            Calculate and return the area of the square.

            Returns:
                int: The area of the square.

        size(self):
            Get the size of the square's sides.

            Returns:
                int: The size of the square's sides.

        size(self, value):
            Set the size of the square's sides.

            Args:
                value (int): The new size for the square's sides.

            Raises:
                TypeError: If the provided value is not an integer.
                ValueError: If the provided value is less than 0 (negative).
    """
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Get the size of the square's sides.

        Returns:
            int: The size of the square's sides.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square's sides.

        Args:
            value (int): The new size for the square's sides.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0 (negative).
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
