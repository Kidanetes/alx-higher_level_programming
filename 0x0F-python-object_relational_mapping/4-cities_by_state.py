#!/usr/bin/python3
"""this module contain a python script which
connects to the MySQLdb and run a query
which selects all cities"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    MY_HOST = "localhost"
    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]
    db = MySQLdb.connect(host=MY_HOST, user=MY_USER,
                         passwd=MY_PASS, db=MY_DB, port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities \
                INNER JOIN states ON cities.state_id = states.id;")
    l1 = cur.fetchall()
    for i in l1:
        print(i)
    cur.close()
    db.close()
