#!/usr/bin/python3
""" To JSON string """
import json


def to_json_string(my_obj):
    """
    Serialize an object to a JSON-formatted string.

    This function takes an input object `my_obj` and converts it into
    a JSON-formatted string representation.
    JSON (JavaScript Object Notation) is a lightweight data interchange
    format commonly used for data storage and exchange between systems.

    Parameters:
        my_obj (Any): The Python object to be serialized to a JSON string.

    Returns:
        str: A JSON-formatted string representing the serialized object.

    Example:
        >>> to_json_string({'name': 'John', 'age': 30})
        '{"name": "John", "age": 30}'
    """
    return json.dumps(my_obj)
