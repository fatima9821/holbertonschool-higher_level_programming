#!/usr/bin/python3
"""Returns True if the object is an instance or False"""


def inherits_from(obj, a_class):
    """define function"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
