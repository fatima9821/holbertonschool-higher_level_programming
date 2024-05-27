#!/usr/bin/python3
"""
le script est une fonction qui lit le contenu
dun fichier texte(UTF8) dans la sortie stantard
"""


def read_file(filename=""):
    """lire le contenu du fichier et l'afficher
    Args:
    filename: le chemin vers le fichier a lire
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
