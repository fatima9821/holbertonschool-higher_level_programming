#!/usr/bin/python3
"""
defines a function that read the file
"""


def read_file(filename=""):
    """function that read the file"""
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
