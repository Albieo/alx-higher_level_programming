#!/usr/bin/python3
""" Square Class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class representing a square, which is a special case of a rectangle with equal side lengths.

    Inherits from the Rectangle class and extends it to represent squares.

    Attributes:
        size (int): The length of each side of the square.
        x (int, optional): The x-coordinate of the square's top-left corner. Default is 0.
        y (int, optional): The y-coordinate of the square's top-left corner. Default is 0.
        id (int or None, optional): An identifier for the square. Default is None.

    Methods:
        __init__(self, size, x=0, y=0, id=None):
            Initializes a new Square object.

            Args:
                size (int): The length of each side of the square.
                x (int, optional): The x-coordinate of the square's top-left corner. Default is 0.
                y (int, optional): The y-coordinate of the square's top-left corner. Default is 0.
                id (int or None, optional): An identifier for the square. Default is None.

            Note:
                The square's width and height are both set to the provided size.

        __str__(self):
            Return a string representation of the shape object in the format:
            "[ClassName] (ID) X/Y - Size"

        size (property):
            Gets the size of the square.

        size (setter):
            Sets the size perimeter of the square.

        update(self, *args, **kwargs):
            Update the attributes of an object of this class using positional arguments (*args)
            and keyword arguments (**kwargs).

        to_dictionary(self):
            Returns a dictionary representation of the Square.

    Inherits:
        Rectangle: This class inherits properties and methods from the Rectangle class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        """
        Return a string representation of the shape object in the format:
        "[ClassName] (ID) X/Y - Size"

        - [ClassName]: The name of the class to which the shape object belongs.
        - (ID): The unique identifier of the shape.
        - X: The X-coordinate of the shape's position.
        - Y: The Y-coordinate of the shape's position.
        - Size: The size of the shape.

        """
        class_name = self.__class__.__name__
        id = self.id
        x = self.x
        y = self.y
        size = self.size
        return "[{}] ({}) {}/{} - {}".format(class_name, id, x, y, size)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the Square.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
            """
            Update the attributes of an object of this class using positional arguments (*args)
            and keyword arguments (**kwargs).

            This method allows updating the object's attributes using either positional arguments or
            keyword arguments. When using positional arguments, the order of arguments
            should be (id, size, x, y).

            Parameters:
            - args (*args): Positional arguments for updating object attributes.
                            The order should be (id, size, x, y).

            - kwargs (**kwargs): Keyword arguments for updating object attributes.
                                Supported keywords are 'id', 'size', 'x', and 'y'.

            Note:
            - When using both positional and keyword arguments, positional arguments take precedence
            over keyword arguments for attribute updates.

            """
            if args:
                if len(args) >= 1:
                    self.id = args[0]
                if len(args) >= 2:
                    self.size = args[1]
                if len(args) >= 3:
                    self.x = args[2]
                if len(args) >= 4:
                    self.y = args[3]
            else:
                if "id" in kwargs:
                    self.id = kwargs['id']
                if "size" in kwargs:
                    self.size = kwargs['size']
                if "x" in kwargs:
                    self.x = kwargs['x']
                if "y" in kwargs:
                    self.y = kwargs['y']

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Square.
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
