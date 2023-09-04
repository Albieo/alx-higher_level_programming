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

    Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(5, 7)
        12
        >>> add_integer(5.2, 7.5)
        12
        >>> add_integer(100.3, -2)
        98
        >>> add_integer(4, "School")
        b must be an integer
        >>> add_integer(None)
        a must be an integer
        >>> add_integer(2)
        100
        >>> add_integer(0)
        98
        >>> add_integer(0,0)
        0

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
        return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()