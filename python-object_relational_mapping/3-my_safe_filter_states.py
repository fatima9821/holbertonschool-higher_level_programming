#!/usr/bin/python3
"""Displays all values in the states table where name matches the argument"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Database connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset='utf8'
    )

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to select states where name matches the argument
    try:
        # Execute the SQL command with the user input as parameter
        sql_query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
        cursor.execute(sql_query, (state_name,))

        # Fetch all the rows in a list of tuples
        results = cursor.fetchall()

        # Print the results
        for row in results:
            print(row)

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the database connection
        db.close()
