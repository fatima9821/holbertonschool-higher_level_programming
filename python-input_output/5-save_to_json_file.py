#!/usr/bin/python3
"""
ce script est une fonction qui ecrit un
obj dans un fichier txt en utilisant json

"""
import json


def save_to_json_file(my_obj, filename):
    """
    fonction qui renvoie un obj dans
    un fichier txt en utilisant json

    """
    with open(filename, "w", encoding="utf-8") as outfile:
        json.dump(my_obj, outfile)
