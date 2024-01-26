#!/usr/bin/python3
"""A script that searches for states in the hbtn_0e_0_usa database"""
import sys
import MySQLdb


def filter_states(username, password, database, state_name):
    """
    Connects to MySQL database and searches
    for states based on user input
    """

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

        # Use format to create SQL query with user input
        query = "SELECT * FROM states WHERE name LIKE \
                '{}' ORDER BY id ASC".format(state_name)
        cursor.execute(query)

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
    # Check if four arguments are provided
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py \
                <username> <password> <database> <state_name>")
        sys.exit(1)

    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Search and display states where name matches the provided argument
    filter_states(username, password, database, state_name)
