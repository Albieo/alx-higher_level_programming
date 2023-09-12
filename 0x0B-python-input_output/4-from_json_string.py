#!/usr/bin/python3
""" From JSON string to Object """
import json


def from_json_string(my_str):
    """
    Deserialize a JSON-formatted string to a Python object.

    This function takes a JSON-formatted string as input and converts it into a
    corresponding Python object. The input string should represent a valid JSON
    object or array.

    Args:
        my_str (str): A JSON-formatted string to be deserialized.

    Returns:
        obj: The Python object representing the deserialized JSON data.

    Raises:
        ValueError: If the input string is not valid JSON.

    Example:
        >>> json_str = '{"name": "John", "age": 30, "city": "New York"}'
        >>> from_json_string(json_str)
        {'name': 'John', 'age': 30, 'city': 'New York'}
    """
    return json.loads(my_str)
