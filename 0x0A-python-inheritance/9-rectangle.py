#!/usr/bin/python3
""" Rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle, a subclass of BaseGeometry, with width
    and height attributes.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance with the specified
        width and height.

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

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle, which is the product
                 of its width and height.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the Rectangle object.

        Returns:
            str: A string in the format "[Rectangle] width/height".
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
