#!/usr/bin/python3
"""
ce script est une fonction qui qui renvoie
un obj represente par une chaine json
"""
import json


def from_json_string(my_str):
    """
    fonctio, qui renvoie un obj en chaine json

    """
    json_str = json.loads(my_str)
    return json_str
