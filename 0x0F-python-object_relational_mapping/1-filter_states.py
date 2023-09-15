#!/usr/bin/python3
""" This module filters the query for state starting from 'N' """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    dbInstance = MySQLdb.connect(user=argv[1],
                                 password=argv[2],
                                 db=argv[3],
                                 # TODO change to localhost
                                 host="localhost",
                                 port=3306)

    cursor = dbInstance.cursor()
    cursor.execute(
        """SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id"""
    )
    data = cursor.fetchall()
    for row in data:
        print(row)
