#!/usr/bin/python3
"""
fonction ecrit une classe
qui definit un student
"""


class Student:
    """une class representative de student"""

    def __init__(self, first_name, last_name, age):
        """Initialisation une new instance"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            new_attr = {}
            for i in attrs:
                if i in self.__dict__:
                    new_attr[i] = self.__dict__[i]
            return new_attr
