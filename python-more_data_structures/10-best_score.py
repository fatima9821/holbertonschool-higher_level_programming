#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary or a_dictionary is None:
        return (None)

    best_value = float('-inf')
    best_key = None

    for key, value in a_dictionary.items():
        if value > best_value:
            best_value = value
            best_key = key

    return (best_key)
