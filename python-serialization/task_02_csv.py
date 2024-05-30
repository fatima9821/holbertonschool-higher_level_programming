#!/usr/bin/env python3
"""
convertir des donnes CSV en format json
"""
import csv
import json


def convertir_csv_en_json(f):
    try:
        data = []
        with open(f, 'r', encoding='utf-8') as fc:

            csv_reader = csv.DictReader(fc)

            data.append(row)

        with open('data.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, indent=4))

        return True

    except FileNotFoundError:
        return False
