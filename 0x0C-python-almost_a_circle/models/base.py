#!/usr/bin/python3
""" Base class """


class Base():
    """
    Base class for creating objects with unique identifiers.

    This class provides a simple mechanism for creating objects with unique identifiers.
    Each object is assigned a unique ID, which is either provided during initialization or
    automatically generated if not provided.

    Attributes:
        __nb_objects (int): A class-level variable to keep track of the number of objects
                            created from this class.

    Methods:
        __init__(self, id=None):
            Initializes a new Base object.

            Args:
                id (int, optional): An optional parameter to specify a custom ID for the
                                    object. If not provided, a unique ID is automatically
                                    generated.

    Attributes:
        id (int): The unique identifier for the object.

    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
