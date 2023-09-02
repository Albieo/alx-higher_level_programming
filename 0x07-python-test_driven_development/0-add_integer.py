#!/usr/bin/python3
""" Integers addition """


def add_integer(a, b=98):
    """Function that adds 2 integers

    Note:
        if args a or b are of type float the program
        would convert the values to of type int.

    Args:
        a (int, float): first number to be added.
        b (int, float): second number to be added.

    Returns:
        the sum of int a and b.

    Raises:
        TypeError: if arguments are not of type int or float.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
        return a + b
