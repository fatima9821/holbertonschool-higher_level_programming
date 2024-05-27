#!/usr/bin/python3

"""
ce scrip est une fonction qui ecrit
une chaine dans un fichier texte
"""


def write_file(filename="", text=""):
    """
    ecrire une chaine dans un fichier txt
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
