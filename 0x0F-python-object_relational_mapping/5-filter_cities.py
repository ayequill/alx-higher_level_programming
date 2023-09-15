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
                                     host="127.0.0.1",
                                     port=3306)

        cursor = dbInstance.cursor()
        cursor.execute(
            """SELECT cities.name
            FROM cities
            INNER JOIN
            states on
            states.id = cities.state_id
            WHERE states.name
             LIKE %s""",
            (argv[4],)
        )

        data = cursor.fetchall()

        for row in data:
            print(row[0])

    except MySQLdb.Error as e:
        print(e)
    finally:
        cursor.close()
        dbInstance.close()
