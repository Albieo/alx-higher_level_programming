#!/usr/bin/python3
""" Read file """


def read_file(filename=""):
    """
    Reads and prints the contents of a text file line by line.

    Args:
        filename (str): The name of the file to be read. If not provided,
            an empty string is used, which will result in an error when
            attempting to open the file.

    """
    with open(filename, "r") as file:
        print(file.read())
