#!/usr/bin/python3
"""  a script that lists all cities from the database hbtn_0e_4_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()

    cur.execute("SELECT * FROM cities INNER JOIN states ON states.id=cities.state_id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()