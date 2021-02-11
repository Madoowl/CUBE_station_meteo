from psycopg2._psycopg import OperationalError
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import Table, Column, String, MetaData
from sqlalchemy_utils import functions
from sqlalchemy import insert, select
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from datetime import datetime

# definition variables
dbDialect = "postgresql"
dbOrm = "psycopg2"
dbUser = "postgres"
dbPassword = "test123"
dbHost = "127.0.0.1"
dbPort = "5432"
# dbBase = "COMMANDES"  #  todo : create binds attached to specific tables or DB "https://flask-sqlalchemy.palletsprojects.com/en/2.x/binds/"
# dbBase = "postgres"
dbBase = "IOTPROD"
dbSchema = "test"

class MyDbConn:
    '''create conn object to db'''

    def __init__(self): #db connexion with file config
        try:
            dbString = f'postgresql+psycopg2://{dbUser}:{dbPassword}@{dbHost}:{dbPort}/{dbBase}'
            if not functions.database_exists(dbString):
                functions.create_database(dbString)
        except OperationalError:
            functions.create_database(dbString)

        self.engine = create_engine(dbString)
        self.conn = self.engine.connect()
        self.metadata = self.MetaData(schema=dbSchema)
        self.metadataR = self.metadata.reflect(self.engine)
        self.Base = self.automap_base(metadata=self.metadata)  # to map the current DB, specify metadata
        self.BaseR = self.Base.prepare(self.engine, reflect=True)  # ,only=['rdv_covid'] )

        # return engine, conn, metadata, metadataR, Base, BaseR

    def dispose(self):
        engine.close()


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

