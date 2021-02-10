# connexion to BD PG
# import sqlalchemy

import psycopg2
from psycopg2 import Error

# conn infos
# TODO : external info file to write

dbUser = "postgres"
dbPassword = "test123"
dbHost = "127.0.0.1"
dbPort = "5432"
dbBase = "postgres"
# connection = None
try:
    # Connect to an existing database
    connection = psycopg2.connect(user=dbUser,
                                  password=dbPassword,
                                  host=dbHost,
                                  port=dbPort,
                                  database=dbBase)
    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    cursor.execute("SELECT version();")
    # Fetch result
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)

# finally:
# if (connection):
#   cursor.close()
#  connection.close()
# print("PostgreSQL connection is closed")
