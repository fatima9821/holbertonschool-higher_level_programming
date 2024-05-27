#!/usr/bin/python3
"""
ce script est une fonction qui renvoie
la representation JSON dun objet

"""


def to_json_string(my_obj):
    json_str = json.dumps(my_obj)
    return json_str
