#!/usr/bin/python3
""" Class to JSON """


def class_to_json(obj):
    """
    Converts a Python object into a dictionary with selected data types.

    This function takes an object as input and creates a dictionary containing
    key-value pairs from the object's attributes. Only attributes with values
    of types int, str, bool, list, or dict will be included in the resulting
    dictionary.

    Args:
        obj: The input Python object to be converted into a dictionary.

    Returns:
        dict: A dictionary containing selected key-value pairs
              from the input object.

    Example:
        >>> class_to_json(Person("Alice", 30, True, ["apple", "banana"]))
        {'name': 'Alice', 'age': 30,
        'is_adult': True, 'fruits': ['apple', 'banana']}
    """
    obj_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (int, str, bool, list, dict)):
            obj_dict[key] = value

    return obj_dict
