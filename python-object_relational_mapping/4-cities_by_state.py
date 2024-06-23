#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""

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

    # Prepare SQL query to select cities
    try:
        sql_query = "SELECT cities.id, cities.name, states.name FROM cities\
                     INNER JOIN states ON cities.state_id = states.id\
                     ORDER BY cities.id ASC"

        # Execute the SQL command
        cursor.execute(sql_query)

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
