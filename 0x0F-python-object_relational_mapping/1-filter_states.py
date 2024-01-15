#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb


def filter_states(username, password, database):
    """Connects to MySQL database and lists states starting with 'N'"""

    try:
        # Connect to MySQL database
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        cursor = db.cursor()

        # Execute SQL query to select states starting with 'N'
        cursor.execute("SELECT * FROM states \
                WHERE name LIKE 'N%' ORDER BY id ASC")

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Display results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        # Close cursor and database connection
        if 'db' in locals() and db:
            cursor.close()
            db.close()


if __name__ == "__main__":
    # Check if three arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./1-filter_states.py \
                <username> <password> <database_name>")
        sys.exit(1)

    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # List and display states starting with 'N'
    filter_states(username, password, database_name)
