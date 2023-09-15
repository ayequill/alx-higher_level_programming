#!/usr/bin/python3
""" This module lists cities from the db """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    dbInstance = MySQLdb.connect(user=argv[1],
                                 password=argv[2],
                                 db=argv[3],
                                 # TODO change to localhost
                                 host="127.0.0.1",
                                 port=3306)

    cursor = dbInstance.cursor()
    cursor.execute(
        """SELECT cities.id, cities.name, states.name FROM 
        cities LEFT JOIN states ON state_id = states.id ORDER BY cities.id"""
    )

    data = cursor.fetchall()

    for row in data:
        print(row)