# https://stackoverflow.com/questions/35684400/how-to-use-python-3-5-1-with-a-mysql-database - Connector
# https://stackoverflow.com/questions/372885/how-do-i-connect-to-a-mysql-database-in-python - Misc
# Good general Guide: https://www.tutorialspoint.com/python/python_database_access.htm

import pymysql


def dbConnect():
    db = pymysql.connect(host="localhost",    # your host, usually localhost
                         user="root",         # your username
                         passwd="test",       # your password
                         db="sonoo")          # name of the data base
    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()
    query = "SELECT * FROM emp"
    # Use all the SQL you like
    try:
        cur.execute(query)
        # print all the first cell of all the rows
        for row in cur.fetchall():
            iId = row[0]
            sName = row[1]
            rAge = row[2]
            print(iId, sName, rAge)
    except:
        print("Error: unable to fetch data")
        db.rollback()
    db.close()

dbConnect()


