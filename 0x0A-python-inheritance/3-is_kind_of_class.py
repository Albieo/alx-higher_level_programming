#!/usr/bin/python3
""" Same class or inherit from """


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a given class or a subclass thereof.

    Args:
        obj: The object to be checked.
        a_class: The class (or type) to check if the object is an instance of.

    Returns:
        bool: True if the object is an instance of the specified class
              or a subclass, False otherwise.
    """
    return isinstance(obj, a_class)
