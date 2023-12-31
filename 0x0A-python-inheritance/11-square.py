#!/usr/bin/python3
""" Square #2 """
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

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square, which is equal to the size squared.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return a string representation of the Square object.

        Returns:
            str: A string in the format "[Square] width/height".
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
