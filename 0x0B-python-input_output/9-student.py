#!/usr/bin/python3
""" Student to JSON """


class Student():
    """
    Represents a student with a first name, last name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        :param first_name: The first name of the student.
        :type first_name: str
        :param last_name: The last name of the student.
        :type last_name: str
        :param age: The age of the student.
        :type age: int
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Converts the student object to a JSON-compatible dictionary.

        :return: A dictionary representation of the student object.
        :rtype: dict
        """
        return self.__dict__
