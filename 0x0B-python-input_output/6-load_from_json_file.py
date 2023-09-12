#!/usr/bin/python3
""" Create object from a JSON file """
import json


def load_from_json_file(filename):
    """
    Load data from a JSON file.

    This function takes a filename as input, opens the file in read mode,
    reads the JSON data from it, and returns the parsed data as a Python
    object.

    Args:
        filename (str): The name of the JSON file to load data from.

    Returns:
        dict or list: A Python dictionary or list containing the parsed
        JSON data from the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON data.
        IOError: If there is an issue reading the file.

    Example:
        >>> data = load_from_json_file("data.json")
    """
    with open(filename, "r") as file:
        return json.loads(file.read())
