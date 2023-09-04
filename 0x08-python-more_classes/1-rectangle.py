#!/usr/bin/python3
""" Simple rectangle """


class Rectangle():
    """
    A class representing a rectangle shape.

    This class provides a simple way to create a rectangle.

    Attributes:
        __width (int): The size of the width.
        __height (int): The size of the height.

    Methods:
        __init__(self, width=0, height=0):
            Initializes a new rectangle object with
            a specified width and height.

            Args:
                width (int, optional): The width of the rectangle
                                       (default is 0).
                height (int, optional): The height of the rectangle
                                       (default is 0).

        width(self):
            Get the width of the rectangle.

            Returns:
                int: The width of the rectangle.

        width(self, value):
            Set the width of the rectangle.

            Args:
                value (int): The new width of the rectangle.

            Raises:
                TypeError: If the provided value is not an integer.
                ValueError: If the provided value is less than 0 (negative).

        height(self):
            Get the height of the rectangle.

            Returns:
                int: The height of the rectangle.

        height(self, value):
            Set the height of the rectangle.

            Args:
                value (int): The new height of the rectangle.

            Raises:
                TypeError: If the provided value is not an integer.
                ValueError: If the provided value is less than 0 (negative).

    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.

        """
        return self.__width

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0 (negative).
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
            Set the height of the rectangle.

            Args:
                value (int): The new height of the rectangle.

            Raises:
                TypeError: If the provided value is not an integer.
                ValueError: If the provided value is less than 0 (negative).
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
