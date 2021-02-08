# import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import Table, Column, String, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker, Session
import psycopg2
from psycopg2 import Error

# definition variables
dbDialect = "postgresql"
dbOrm = "psycopg2"
dbUser = "postgres"
dbPassword = "test123"
dbHost = "127.0.0.1"
dbPort = "5432"
#dbBase = "COMMANDES"
dbBase = "postgres"

# dbString = f"{dbDialect}+{dbOrm}://{dbUser}:{dbPassword}@{dbHost}:{dbPort}/{dbBase}"
dbString = f'postgresql+psycopg2://{dbUser}:{dbPassword}@{dbHost}:{dbPort}/{dbBase}'

# exploitation base

engine = create_engine(dbString)

# mapping current DB from PG
Base = automap_base()  # to map the current DB
Base.prepare(engine, reflect=True)  # ,only=['rdv_covid'] )

metadata = MetaData(engine)
metadata.reflect(engine)

# lTablesNames = base.classes.keys()

# create object from DB

# rdv_covid = Base.classes.rdv_covid
# tableTest = Base.classes.clients

tableTest = Base.classes.rdvcovid

session = Session(engine)

query = session.query(tableTest).limit(4)
for item in query:
    print(item.nb)


def get_tables(p_engine):
    """ Get tables names from schema
    Should take or retrieve multi scheme """

    for schema in p_engine.table_name():
        pass


print(engine.table_names())
# print(metadata.tables.keys()) #quid many scheme?
# # https://stackoverflow.com/questions/6473925/sqlalchemy-getting-a-list-of-tables
# print(metadata.tables.values())


# nomTable = "rdv_covid"

# db = scoped_session(sessionmaker(bind=engine))
