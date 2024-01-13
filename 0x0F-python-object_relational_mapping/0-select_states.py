#!/usr/bin/python3
import sys
import MySQLdb


if __name__ == "__main__":
    # Checks if three arguments are provided.
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # To connect to MySQLdb 
    try:
        db = MySQLdb.connect(host='localhost', port=3306, user='username', passwd='password', db='db_name')
        cursor = db.cursor()
        # Execute SQL query to select all states sorted by id
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Display results
        for row in rows:
            print(row)

        # close cursor and databse connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        sys.exit(1)
