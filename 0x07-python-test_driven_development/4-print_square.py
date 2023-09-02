#!/usr/bin/python3
""" Print square """


def print_square(size):
    """ A function that prints a square with the character #.

    Args:
        size(int): The input number of # to be printed. This
                    size is the vert and horizontal number.

    Example:
        >>> print_square(3)
        ###
        ###
        ###

    Raises:
        ValueError: if 'size' is less than 0.
        TypeError: if 'size' is a float and is less than 0.

    """
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            print("#" * size)
