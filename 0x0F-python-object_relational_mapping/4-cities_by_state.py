#!/usr/bin/python3
""" This module lists cities from the db """
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
            """SELECT cities.id,
             cities.name,
             states.name FROM
             cities INNER JOIN
             states ON state_id = states.id
             ORDER BY cities.id
             """
        )

        data = cursor.fetchall()

        for row in data:
            print(row)

    except MySQLdb.Error as e:
        print(e)
    finally:
        cursor.close()
        dbInstance.close()
