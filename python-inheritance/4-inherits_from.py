#!/usr/bin/python3
"""
this function return true if the obj is instance or inherited
"""


def inherits_from(obj, a_class):
    """ get the class of the obj """
    obj_class = type(obj)

    """ chech if obj clss is the same """
    if obj_class is a_class:
        return False

    return issubclass(obj_class, a_class)
