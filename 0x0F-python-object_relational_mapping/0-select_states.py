#!/usr/bin/python3
""" A script that lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb


def fetch_states(username, password, database_name):
    """ This function list all states"""
    try:
        # Connect to MySQL database
        db = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=username,
                passwd=password,
                db=database_name
        )
        cursor = db.cursor()

        # Execute SQL query to select all states sorted by id
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Display results in the specified format
        for row in rows:
            print(row)

        # Close cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)


if __name__ == "__main__":
    # Check if three arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py\
                <username> <password> <database_name>")
        sys.exit(1)

    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Fetch and display states
    fetch_states(username, password, database_name)
