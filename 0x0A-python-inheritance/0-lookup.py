#!/usr/bin/python3
def lookup(obj):
    """
    Get a list of attributes and methods associated with the given object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of strings representing the names of attributes
              and methods associated with the object.

    This function returns a list of all the attributes and methods
    available for the provided object.
    """
    return dir(obj)
