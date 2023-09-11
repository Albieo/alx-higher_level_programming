#!/usr/bin/python3
""" Improve Geometry """


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
    """

    def area(self):
        raise Exception("area() is not implemented")
