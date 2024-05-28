#!/usr/bin/python3
"""
script qui ajoute tous les
arguments à une liste Python,
puis enregistrez-les dans un fichier
"""
from sys import argv


save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file
filename = "add_item.json"
try:
    list = load(filename)
except Exception:
    list = []
for argumments in argv[1:]:
    list.append(argumments)
save(list, filename)
