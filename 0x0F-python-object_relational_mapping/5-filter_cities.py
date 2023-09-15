#!/usr/bin/python3
""" This module lists cities from the db that matches the
    state passed as arg
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    try:
        dbInstance = MySQLdb.connect(user=argv[1],
                                     password=argv[2],
                                     db=argv[3],
                                     # TODO change to localhost
                                     host="localhost",
                                     port=3306)

        cursor = dbInstance.cursor()
        cursor.execute(
            """SELECT cities.name
            FROM cities
            LEFT JOIN
            states on
            states.id = cities.state_id
            WHERE states.name
             LIKE %s""",
            (argv[4],)
        )

        data = cursor.fetchall()

        print(*[row[0] for row in data], sep=', ')

    except MySQLdb.Error as e:
        print(e)
    finally:
        cursor.close()
        dbInstance.close()
