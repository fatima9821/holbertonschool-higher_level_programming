#!/usr/bin/python3
"""Write the first class Base"""

import json


class Base:
    """the base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """define init method"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string representation."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """return the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []

        # Get the class name
        class_name = cls.__name__

        # create the filename
        filename = "{}.json".format(class_name)

        # Convert list_objs to a list of dictionaries
        list_dicts = [obj.to_dictionary() for obj in list_objs]

        # Convert the list of dictionaries to JSON string
        json_str = cls.to_json_string(list_dicts)

        # write the JSON string to the file
        with open(filename, "w") as file:
            file.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        # create a "dummy" instance with a mandatory attributes.
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            return None

        # call the update method to apply the real vallue
        dummy_instance.update(**dictionary)

        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file."""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as file:
                json_str = file.read()
        except FileNotFoundError:
            return []

        list_dicts = cls.from_json_string(json_str)
        list_instances = [cls.create(**d) for d in list_dicts]

        return list_instances
