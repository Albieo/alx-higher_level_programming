#!/usr/bin/python3
""" Read file """


def read_file(filename=""):
    """
    Reads and prints the contents of a text file line by line.

    Args:
        filename (str): The name of the file to be read. If not provided,
            an empty string is used, which will result in an error when
            attempting to open the file.

    Raises:
        FileNotFoundError: If the specified file does not exist or
                           cannot be found.
        IsADirectoryError: If the provided filename refers to a directory
                           instead of a regular file.

    """
    with open(filename) as file:
        print(file.read())
