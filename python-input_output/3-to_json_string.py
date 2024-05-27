#!/usr/bin/python3
"""
ce script est une fonction qui renvoie
la representation JSON dun objet

"""
import json


def to_json_string(my_obj):
    """
    fonction qui renvoie la representation json
    """

    json_str = json.dumps(my_obj)
    return json_str
