#!/usr/bin/env python3
"""
convertir des donnes CSV en format json
"""
import json
import csv


def convertir_csv_en_json(nom_fichier_csv):
    try:

        with open(nom_fichier_csv, mode='r', newline='', encoding='utf-8')
        as fichier_csv:

            lecteur_csv = csv.DictReader(fichier_csv)

            donnees = list(lecteur_csv)

        with open('data.json', mode='w', encoding='utf-8') as fichier_json:
            json.dump(donnees, fichier_json, indent=4)

        return True

    except FileNotFoundError:
        return False
