#!/usr/bin/python3
""" This script connects to the db and list all states in the database"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(user=argv[1],
                         password=argv[2],
                         db=argv[3],
                         host="127.0.0.1",
                         port=3306)

    # Create a cursor pointer to interact with the database
    cursor = db.cursor()
    cursor.execute(
        """SELECT * FROM states ORDER BY states.id"""  # Executing the query
    )

    # Fetch response
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
