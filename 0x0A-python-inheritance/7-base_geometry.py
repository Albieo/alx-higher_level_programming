#!/usr/bin/python3
""" Integer validator """


class BaseGeometry():
    """
    This is the base class for geometry-related operations.
    It serves as a foundation for more specialized geometry classes.

    Methods:
    --------
    area(self)
        Calculate the area of the geometry object.

        Raises:
        -------
        Exception
            This method is not implemented in the base class and should
            be overridden in derived classes to provide specific
            implementations for calculating the area.

    integer_validator(self, name, value)
        Validates an integer value for a specific attribute.

        Parameters:
        -----------
        name : str
            The name of the attribute being validated.

        value : int
            The value to be validated as an integer.

        Raises:
        -------
        TypeError
            If the provided value is not an integer.

        ValueError
            If the provided integer value is less than or equal to 0.
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
        self.value = value
