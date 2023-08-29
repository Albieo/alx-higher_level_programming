#!/usr/bin/python3
"""Define a class Square."""


class Square():
    """
    A class representing a square shape.

    Attributes:
    __size (int): The size of the square.
    __position (tuple): The position of the square on a grid.

    Methods:
    __init__(self, size=0, position=(0, 0)):
        Initializes a new Square instance with a specified size and position.

    area(self):
        Calculate and return the area of the square.

    size (property):
        Get the size of the square.

    size (setter):
        Set the size of the square. Must be a non-negative integer.

    position (property):
        Get the position of the square as a tuple of 2 positive integers.

    position (setter):
        Set the position of the square. Must be a tuple of 2 positive integers.

    my_print(self):
        Print a visual representation of the square on the console.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Get the position of the square as a tuple of 2 positive integers.

        Returns:
        tuple: The position of the square as (x, y).
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
        value (tuple): The new position as a tuple of
                        2 positive integers (x, y).

        Raises:
        TypeError: If value is not a tuple of 2 positive integers.
        """
        if isinstance(value, tuple) and len(value) == 2:
            if all(isinstance(val, int) and val >= 0 for val in value):
                self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Print a visual representation of the square on the console.
        """
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1])
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
