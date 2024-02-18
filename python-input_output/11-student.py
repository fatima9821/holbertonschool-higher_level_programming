#!/usr/bin/python3
"""The Student class"""


class Student:
    """The Student Class"""

    def __init__(self, first_name, last_name, age):
        """Create a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Class student to JSON"""
        if attrs is None:
            return self.__dict__
        dic = {}
        for i in attrs:
            if i in self.__dict__:
                dic[i] = self.__dict__[i]
        return dic

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for attrs in json:
            self.__dict__[attrs] = json[attrs]
