#!/usr/bin/python3
"""
this function return True or False if the object is an instance
"""


def is_same_class(obj, a_class):
    """ check if obj is an instance of a_class """
    return type(obj) is a_class
