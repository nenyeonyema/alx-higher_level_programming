#!/usr/bin/python3
""" a script that lists all cities from the database hbtn_0e_4_usa"""
import sys
import MySQLdb


def cities_by_state(username, password, database):
    """Connects to MySQL database and lists all cities by state"""
    try:
        db = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=username,
                passwd=password,
                db=database
                )
        cursor = db.cursor()

        query = "SELECT cities.id, cities.name, states.name FROM \
                cities JOIN states ON cities.state_id = states.id \
                ORDER BY cities.id ASC"

        cursor.execute(quuery)

        rows = cursor.fetchall()

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
        print("Usage: ./4-cities_by_state.py \
                <username> <password> <database_name>")
        sys.exit(1)

    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # List and display all cities by state
    cities_by_state(username, password, database_name)
