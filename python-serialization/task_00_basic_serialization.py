#!/usr/bin/env python3
"""
creation de module de sterelisation
dun dic dans un json
"""
import json


def serialize_and_save_to_file(data, filename):
    with open(filename, "w", encoding="utf-8") as outfile:
        json.dump(data, outfile)

def load_and_deserialize(filename):
    with open(filename, "r", encoding="utf-8") as infile:
        return json.load(infile)
