#!/usr/bin/python3
""" Save Object to a file """
import json


def save_to_json_file(my_obj, filename):
    """
    Serialize the given Python object `my_obj` to a JSON-formatted string
    and save it to the specified `filename`.

    Args:
        my_obj (Any): The Python object to be serialized to JSON.
        filename (str): The name of the file where the JSON data will be saved.

    Raises:
        FileNotFoundError: If the specified `filename` or its parent directory
                           does not exist.
        PermissionError: If the user does not have permission to
                         write to the file.
        TypeError: If `my_obj` cannot be serialized to JSON.

    Example:
        # Serialize a dictionary and save it to a file
        data = {'name': 'John', 'age': 30}
        save_to_json_file(data, 'data.json')
    """
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
