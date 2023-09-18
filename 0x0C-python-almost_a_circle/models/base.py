#!/usr/bin/python3
""" Base class """


class Base():
    """
    Base class for creating objects with unique identifiers.

    This class provides a simple mechanism for creating objects with unique
    identifiers.
    Each object is assigned a unique ID, which is either provided during
    initialization or automatically generated if not provided.

    Attributes:
        __nb_objects (int): A class-level variable to keep track of the number
                            of objects created from this class.

    Methods:
        __init__(self, id=None):
            Initializes a new Base object.

            Args:
                id (int, optional): An optional parameter to specify a custom
                                    ID for the object. If not provided, a
                                    unique ID is automatically generated.

        Static Methods:
            to_json_string(list_dictionaries):
                Converts the list_dictionaries and returns the JSON
                string representation of list_dictionaries.

                Args:
                    list_dictionaries (list): list of dictionaries.

                Return:
                    The JSON string representation of list_dictionaries.
                    If list is None return the str "[]"

            from_json_string(json_string):
                Converts the json string and returns a list of JSON string
                representation.

                Args:
                    json_string (str): a string representing a list of
                                       dictionaries.

                Return:
                    The list represented by json_string or an empty list if
                    json_string is none or empty.

        Class Methods:
            save_to_file(cls, list_objs):
                Write the JSON string representation of list_objs to a file.

                Args:
                    list_objs (list): a list of instances who inherits of
                                      Base class.

            create(cls, **dictionary):
                Create an instance with attributes set from the provided
                dictionary.

                Args:
                    **dictionary: dictionary can be thought of as a double
                                  pointer to a dictionary.
                Return:
                    An instance with all attributes already set.

            load_from_file(cls):
                Load instances from a JSON file and return a list of instances.

                Return:
                    return a list of instances - the type of these instances
                    depends on cls. Or an empty list if file doesn't exist.

    Attributes:
        id (int): The unique identifier for the object.

    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts the list_dictionaries and returns the JSON
        string representation of list_dictionaries.
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.
        """
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        filename = "{}.json".format(class_name)
        list_dicts = [obj.to_dictionary() for obj in list_objs]

        with open(filename, "w") as file:
            file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Converts the json string and returns a list of
        JSON string representation.
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes set from the provided dictionary.
        """
        class_name = cls.__name__

        if class_name == "Rectangle":
            dummy_instance = cls(1, 1)
        if class_name == "Square":
            dummy_instance = cls(1, 1)

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Load instances from a JSON file and return a list of instances.
        """
        class_name = cls.__name__
        filename = "{}.json".format(class_name)

        with open(filename, "r") as file:
            dict_list = cls.from_json_string(file.read())

        if not dict_list:
            return []

        return [cls.create(**d) for d in dict_list]
