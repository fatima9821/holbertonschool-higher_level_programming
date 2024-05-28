#!/usr/bin/python3
"""
fonction qui creer un obj
"""
import json


def load_from_json_file(filename):
    """ creation de obj """
    with open(filename, 'r') as file:
        return json.load(file)
