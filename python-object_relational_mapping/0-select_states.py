#!/usr/bin/python3
import MySQLdb
import sys
from sys import argv


if __name__ == '__main__':
    """
    Access the database and get the states
    from the database.
    """
    # Connexion à la base de données
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    # Créaton of curseur to execute the  SQL
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # get the result
    rows = cur.fetchall()

    # display the result
    for row in rows:
        print(row)

    # close the curseur to data base connected
    cur.close()
    db.close()
