#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    Check if the given object belongs to the specified class.

    Args:
        obj: Any object.
        a_class: A Python class or type to compare with.

    Returns:
        bool: True if the object is an instance of the specified class,
              otherwise False.

    Example:
        >>> is_same_class(5, int)
        True
        >>> is_same_class("Hello", int)
        False
    """
    return type(obj) is a_class
