#!/usr/bin/python3
"""  Write to a file """


def write_file(filename="", text=""):
    """
    Write text to a file specified by the given filename.

    Parameters:
        filename (str): The name of the file to write to. If not provided,
                        an empty string is used.
        text (str): The text to be written to the file. If not provided,
                    an empty string is used.

    Return:
        The number of characters written.

    """
    with open(filename, "w") as file:
        file.write(text)
    return len(text)
