#!/usr/bin/python3
""" Rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle, a subclass of BaseGeometry, with width and
    height attributes.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance with the specified width
        and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            ValueError: If either width or height is not a positive integer.
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
