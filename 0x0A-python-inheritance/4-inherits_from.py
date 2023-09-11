#!/usr/bin/python3
""" Only sub class of """


def inherits_from(obj, a_class):
    """
    Check if an object inherits from a specified class.

    This function checks whether the given object is an instance of
    the specified class or one of its subclasses, but not the exact
    class itself.

    Args:
        obj: The object to be checked for inheritance.
        a_class: The class to check for inheritance from.

    Returns:
        bool: True if the object inherits from the specified class,
              False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
