import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import Table, Column, String, MetaData, insert
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
# dbBase = "COMMANDES"  #  todo : create binds attached to specific tables or DB "https://flask-sqlalchemy.palletsprojects.com/en/2.x/binds/"
# dbBase = "postgres"
dbBase = "IOTPROD"
dbSchema = "public"

# dbString = f"{dbDialect}+{dbOrm}://{dbUser}:{dbPassword}@{dbHost}:{dbPort}/{dbBase}"
dbString = f'postgresql+psycopg2://{dbUser}:{dbPassword}@{dbHost}:{dbPort}/{dbBase}'

# exploitation base

engine = create_engine(dbString)
conn = engine.connect()



# mapping current DB from PG
metadata = MetaData(schema=dbSchema)
metadata.reflect(engine)

Base = automap_base(metadata=metadata)  # to map the current DB, specify metadata
Base.prepare(engine, reflect=True)  # ,only=['rdv_covid'] )

# create object from DB

# def tables
tTmpRel = Table('t_rel_test', metadata, autoload_with=engine)
tSonde = Table('t_sonde', metadata, autoload_with=engine)

# init session
session = Session(engine)  # create session

query = sqlalchemy.select([tSonde])
cursor = conn.execute(query)
result = cursor.fetchall()

print(result) #return result


# # newItem = (insert(tTmpRel).values(relid="456", relhumidity=2.3, treltemperature=3.4))
# newItem = tTmpRel.insert().values(relid='456', relhumidity=2.30, reltemperature=3.40)
# print('hello')
# conn.execute(newItem)
#
# session.commit()


# query = session.query(tableTest).limit(4)
# for item in query:
#     print("Hello")
#     # print(item.nom)
#     print(item.nom)


def get_tables(p_engine):
    """ Get tables names from schema
    Should take or retrieve multi scheme """

    for schema in p_engine.table_name():
        pass


# print(engine.table_names())
# print(metadata.tables.keys()) #quid many scheme?
# # https://stackoverflow.com/questions/6473925/sqlalchemy-getting-a-list-of-tables
# print(metadata.tables.values())


# nomTable = "rdv_covid"

# db = scoped_session(sessionmaker(bind=engine))
