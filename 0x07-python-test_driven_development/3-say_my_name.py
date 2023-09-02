#!/usr/bin/python3
""" Say my name """


def say_my_name(first_name, last_name=""):
    """ display name

    This function takes a first only or first and last name and
    prints it to the terminal when called.

    Args:
        first_name (str): The input string to be printed.
        last_name (str): The input string to be printed.

    Example:
        >>> say_my_name("John", "Harvard")
        My name is John Harvard
        >>> say_my_name("John")
        My name is John

        Raises:
            TypeError: If 'first_name' or 'last_name' is not str.

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
