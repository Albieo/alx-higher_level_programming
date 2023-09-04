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


        __str__(self):
            Print a representation of the rectangle using '#' characters.

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

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """
        Print a representation of the rectangle using '#' characters.
        If the width or height is 0, it prints an empty line.

        Returns:
            A string representation of the rectangle as #.
            An empty string if width or height = 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            result = ["#" * self.width for _ in range(self.height)]
            return "\n".join(result)
