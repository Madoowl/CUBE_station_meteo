from flask import Flask, request
from flask_restplus import Resource, Api
import time
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
dbSchema = "test"

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

session = Session(engine)

# Config Flask App Definition
app = Flask(__name__)
api = Api(app=app, version="0.1", doc="/api", title="API station météo", description="Test API station météo",
          default="mon api", default_label='ceci est une api de test', validate=True)


# DEMO with simple api function via HTTP GET in default namespace

@api.route("/api/tempRel/")
class cTmpRel(Resource):
    @api.response(200, 'API Ping : Success')
    @api.response(400, 'API Ping: Error')
    def post(self):
        """
        Add new rel to the DB """

        data = api.payload
        if data == None :
            data = request.get_json()
            print("passé par request")
        print(data)
        print(type(data))
        if not data:
            data = {"response": "ERROR"}
            return data, 404
        else:  # renvoie des données et insertions dans DB
            collecte = data
            cltHumidity = 0.0
            cltTemperature = 0.0
            i = 0

            while i <= (len(collecte) - 1):
                # direct access to specific key to get corresponding values
                cltHumidity += collecte[i].get('hum')
                cltTemperature += collecte[i].get('temp')
                i += 1
            moyHumidity = round(cltHumidity / len(collecte), 1)
            moyTemp = round(cltTemperature / len(collecte), 1)

            table = Table('t_rel_test', metadata, autoload_with=engine)

            newItem = table.insert().values(relid=111, relhumidity=moyHumidity, reltemperature=moyTemp)

            print(str(newItem))
            conn.execute(newItem)
            session.commit()

            msg = {"response": "SUCCESS"}
            return msg, 200

# @api.route("/api/v1/ping")
# class Ping(Resource):
#     @api.response(200, 'API Ping : Success')
#     @api.response(400, 'API Ping: Error')
#     @api.response(403, 'API Ping: Ceci n\'est pas autorisé')
#     def get(self):
#         """
#         Test de l'API avec un simple ping
#         """
#         return {'response': 'pong'}, 200
#
#     @api.response(400, 'API Ping: This is a custom 400 error code')
#     def delete(self):
#         """
#         Test de l'API avec erreur 400
#         """
#         return {'response': 'bad pong'}, 400
#
#     def post(self):
#         """
#         Test de l'API avec erreur 403
#         """
#         return {'response': 'pong'}, 403
#

# @api.route("/api/v1/time")
# class Time(Resource):
#     @api.response(200, 'Flask Time : Success')
#     @api.response(400, 'Flask DateTime: Error')
#     def get(self):
#         """
#         Renvoi la date actuelle et le timestamp
#         """
#         current_timestamp = datetime.datetime.now().timestamp()
#         current_date = datetime.datetime.now()
#         return {'response': {
#             'current_date': str(current_date),
#             'current_timestamp': str(current_timestamp)}
#                }, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
