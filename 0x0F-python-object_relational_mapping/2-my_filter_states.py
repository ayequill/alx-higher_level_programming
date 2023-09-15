#!/usr/bin/python3
""" This module searches for an entry and prints """
from sys import argv

import MySQLdb

if __name__ == "__main__":
    try:
        dbInstance = MySQLdb.connect(user=argv[1],
                                     password=argv[2],
                                     db=argv[3],
                                     # TODO change to localhost
                                     host="localhost",
                                     port=3306)

        cursor = dbInstance.cursor()
        search_item = argv[4]

        cursor.execute("""SELECT * FROM
                       states WHERE name
                       LIKE BINARY '{}'
                       ORDER BY states.id
                       """.format(argv[4]))

        data = cursor.fetchall()
        for row in data:
            print(row)
    except MySQLdb.Error as e:
        print(f"MySQL Error: {e}")
    finally:
        cursor.close()
        dbInstance.close()
