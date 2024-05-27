#!/usr/bin/python3
"""
ce script est une fonction qui ajoute
une chaine a la fin du texte
"""


def append_write(filename="", text=""):
    """
    ajoutez une chaine a la fin du texte

    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
