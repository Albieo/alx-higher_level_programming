#!/usr/bin/python3
""" Append to a file """


def append_write(filename="", text=""):
    """
    Appends the specified text to a file.

    This function opens the file specified by the 'filename' parameter in
    append mode ('a') and appends the provided 'text' to the end of the file.
    If the file does not exist, it will be created. If the file exists, the
    text is added to the existing content.

    Parameters:
        filename (str): The name of the file to which the text will be
                        appended. If not provided, a new file will be created
                        with a default name (an empty string will create
                        a file in the current working directory).
        text (str): The text to append to the file.

    Return:
        The number of characters added.

    Raises:
        OSError: If there is an issue opening or writing to the file.

    """
    with open(filename, "a") as file:
        file.write(text)
    return len(text)
