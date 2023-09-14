#!/usr/bin/python3
""" Student to JSON """


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

    def to_json(self):
        """
        Convert the Student object to a JSON-like dictionary.

        Returns:
            dict: A dictionary containing
                  the student's first name, last name, and age.
        """
        obj_dict = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
        return obj_dict
