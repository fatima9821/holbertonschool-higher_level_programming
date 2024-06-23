#!/usr/bin/python3
"""lists all states with a name starting with N (upper N) from the database"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Database connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

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

    # Prepare SQL query to select states starting with 'N'
    sql_query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"

    try:
        # Execute the SQL command
        cursor.execute(sql_query)

        # Fetch all the rows in a list of tuples
        results = cursor.fetchall()

        # Print the results
        for row in results:
            if 'N' in row[1]:
                print(row)

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the database connection and cursor
        db.close()
