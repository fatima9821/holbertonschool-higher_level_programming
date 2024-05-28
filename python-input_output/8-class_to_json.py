#!/usr/bin/python3
"""
fonction qui renvoie la
description dun dic
"""


def class_to_json(obj):
    """
    Convertit une instance de classe en un dictionnaire
    pour la sérialisation JSON dict: Le dictionnaire représe
    """
    obj_dict = {}

    attributes = vars(obj)

    for attr, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            obj_dict[attr] = value

    return obj_dict
