#!/usr/bin/python3
""" This module filters the query for state starting from 'N' """

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    try:
        dbInstance = MySQLdb.connect(user=argv[1],
                                     password=argv[2],
                                     db=argv[3],
                                     host="localhost",
                                     port=3306)

        cursor = dbInstance.cursor()
        cursor.execute(
            """SELECT *
                FROM states
                WHERE states.name
                LIKE BINARY 'N%'
                ORDER BY states.id
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
