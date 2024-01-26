#!/usr/bin/python3
"""
A script that lists all cities of a
given state from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb


def filter_cities_by_state(username, password, database, state_name):
    """
    Connects to MySQL database and
    lists all cities of a given state
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

        # Use parameterized query to prevent SQL injection
        query = "SELECT cities.name FROM cities JOIN states \
                ON cities.state_id = states.id \
                WHERE states.name = %s ORDER BY cities.id ASC"
        cursor.execute(query, (state_name,))

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Display results
        cities = ', '.join(row[0] for row in rows)
        print(cities)

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
        print("Usage: ./5-filter_cities.py \
                <username> <password> <database> <state_name>")
        sys.exit(1)

    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # List and display all cities of the given state
    filter_cities_by_state(username, password, database, state_name)
