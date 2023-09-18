#!/usr/bin/python3
""" Rectangle Class """
from models.base import Base


class Rectangle(Base):
    """
    A class representing a rectangle, inheriting from the Base class.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the top-left corner of the rectangle.
        y (int): The y-coordinate of the top-left corner of the rectangle.
        id (int): An optional identifier for the rectangle.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
            Initializes a new Rectangle instance with the given width, height,
            and optional position and identifier.

        width (property):
            Get the width of the rectangle.

        width (setter):
            Set the width of the rectangle. Raises a TypeError if
            the value is not an integer, and a ValueError if it's not > 0.

        height (property):
            Get the height of the rectangle.

        height (setter):
            Set the height of the rectangle. Raises a TypeError if
            the value is not an integer, and a ValueError if it's not > 0.

        x (property):
            Get the x-coordinate of the top-left corner of the rectangle.

        x (setter):
            Set the x-coordinate of the top-left corner of the rectangle.
            Raises a TypeError if the value is not an integer,
            and a ValueError if it's not >= 0.

        y (property):
            Get the y-coordinate of the top-left corner of the rectangle.

        y (setter):
            Set the y-coordinate of the top-left corner of the rectangle.
            Raises a TypeError if the value is not an integer,
            and a ValueError if it's not >= 0.

        area(self):
            Returns the area value of the reactangle instance.

        display(self):
            Display the shape by printing it to the console as
            a grid of '#' characters.

        __str__(self):
            Return a string representation of the shape object in the format:
            "[ClassName] (ID) X/Y - Width/Height"

        update(self, *args, **kwargs):
            Update the attributes of an object of this class using
            positional arguments (*args) and keyword arguments (**kwargs).

        to_dictionary(self):
            Returns a dictionary representation of the Rectangle.

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the top-left corner of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x-coordinate of the top-left corner of the rectangle.

        Args:
            value (int): The new x-coordinate value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the top-left corner of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y-coordinate of the top-left corner of the rectangle.

        Args:
            value (int): The new y-coordinate value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__height * self.__width

    def display(self):
        """
        Display the shape by printing it to the console as
        a grid of '#' characters.

        If either the width or height of the shape is 0, it will display
        an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            print("")
        else:
            result = [" " * (self.__width - self.__x)
                      for _ in range(self.__y)] + \
                     [" " * self.__x + "#" * self.__width
                      for _ in range(self.__height)]
            print("\n".join(result))

    def __str__(self):
        """
        Return a string representation of the shape object in the format:
        "[ClassName] (ID) X/Y - Width/Height"

        - [ClassName]: The name of the class to which the shape object belongs.
        - (ID): The unique identifier of the shape.
        - X: The X-coordinate of the shape's position.
        - Y: The Y-coordinate of the shape's position.
        - Width: The width of the shape.
        - Height: The height of the shape.

        """
        class_name = self.__class__.__name__
        id = self.id
        x = self.__x
        y = self.__y
        width = self.__width
        height = self.__height
        return "[{}] ({}) {}/{} - {}/{}".\
            format(class_name, id, x, y, width, height)

    def update(self, *args, **kwargs):
        """
        Update the attributes of an object of this class using positional
        arguments (*args) and keyword arguments (**kwargs).

        This method allows updating the object's attributes using either
        positional arguments or keyword arguments. When using positional
        arguments, the order of arguments should be (id, width, height, x, y).

        Parameters:
        - args (*args): Positional arguments for updating object attributes.
                        The order should be (id, width, height, x, y).

        - kwargs (**kwargs): Keyword arguments for updating object attributes.
                             Supported keywords are 'id', 'width', 'height',
                             'x', and 'y'.

        Note:
        - When using both positional and keyword arguments,
          positional arguments take precedence over keyword arguments
          for attribute updates.

        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            if "id" in kwargs:
                self.id = kwargs['id']
            if "width" in kwargs:
                self.__width = kwargs['width']
            if "height" in kwargs:
                self.__height = kwargs['height']
            if "x" in kwargs:
                self.__x = kwargs['x']
            if "y" in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Rectangle.
        """
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
