#!/usr/bin/python3
""" Student to disk and reload """


class Student():
    """
    A class representing a student with basic information.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Convert the Student object to a dictionary in JSON-like format.

        Args:
            attrs (list, optional): A list of attribute names to include in the
                resulting dictionary. If not provided (default), all attributes
                will be included.

        Returns:
            dict: A dictionary representation of the Student object.

        """
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Update the Student object's attributes from a JSON dictionary.

        Args:
            json (dict): A dictionary containing attribute-value pairs
                         to update the Student object.

        Returns:
            None
        """
        for key, value in json.items():
            setattr(self, key, value)
