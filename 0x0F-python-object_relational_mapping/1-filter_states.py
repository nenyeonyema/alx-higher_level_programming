#!/usr/bin/python3
""" Lists states with N names"""
import sys
import MySQLdb


if __name__ == "__maini__":
    try:
        # Check if correct number of arguments is provided
        if len(sys.argv) != 4:
            raise ValueError("Usage: {} \
                    <username> <password> <database>".format(sys.argv[0]))

        # Extract command line arguments
        username, password, database = sys.argv[1:]

        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8"
        )

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Execute the SQL query to retrieve states starting with 'N'
        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        cursor.execute(query)

        # Fetch all the rows
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(1)

    finally:
        # Close cursor and database connection in the finally block
        if 'db' in locals() and db:
            cursor.close()
            db.close()
