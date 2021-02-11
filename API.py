from flask import Flask, request, jsonify
from flask_restplus import Resource, Api
import time
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import Table, Column, String, MetaData
from sqlalchemy import insert, select
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy.sql import exists
from datetime import datetime
import json
from sqlalchemy.sql import func
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
#dbSchema = "test"
dbSchema = "public"

# dbString = f"{dbDialect}+{dbOrm}://{dbUser}:{dbPassword}@{dbHost}:{dbPort}/{dbBase}"
dbString = f'postgresql+psycopg2://{dbUser}:{dbPassword}@{dbHost}:{dbPort}/{dbBase}'

# définition tables

tReleve = "t_releve"
tSonde = "t_sonde"
tTest = "t_rel_test" #sur schéma test

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
    @api.response(500, 'API Ping : Error')
    def post(self):
        """
        Add new rel to the DB
        """
        # todo : put models to create a db and /or table if does not exist

        data = api.payload
        print('réception de qqch')
        if data is None:
            data = request.get_json()
        if not data:
            data = {"response": "ERROR"}
            return data, 404

        else:
            #  get the average of value sended, insert to DB
            collecte = data
            print(collecte)

            cltHumidity = 0.0
            cltTemperature = 0.0

            # vérification avec table + relation

            idSonde = str(collecte[0]['serial'])
            ipSonde = str(collecte[0]['ip'][0])

            getSonde(pIdSonde=idSonde, pIpSonde=ipSonde)

            # traitement valeurs

            i = 0
            while i <= (len(collecte) - 1):
                # direct access to specific key to get corresponding values
                cltHumidity += collecte[i].get('hum')
                cltTemperature += collecte[i].get('temp')
                i += 1

            moyHumidity = round(cltHumidity / len(collecte), 1)
            moyTemp = round(cltTemperature / len(collecte), 1)
            print(ipSonde)

            #   specific table from DB
            table = Table(tReleve, metadata, autoload_with=engine)
            timestamp = time.time()


            # sql command to insert values
            newItem = table.insert().values(sonid=idSonde, reldatetime=datetime.now(), relhumidity=moyHumidity, reltemperature=moyTemp)
            print(str(newItem))

            #  execute sql commands
            conn.execute(newItem)
            session.commit()

            #  return message
            msg = {"response": "SUCCESS"}
            return msg, 200

    @api.response(200, 'Donnée retournée')
    @api.response(400, 'Erreur accès')
    def get(self):  # param 'self' ?
        """
        return infos
        """
        try:
            table = Table(tReleve, metadata, autoload_with=engine)
            querySQL =  "SELECT id, sonid, TO_CHAR(reldatetime, 'MON-DD-YYYY HH12:MIPM') datetime, reltemperature, relhumidity FROM test.t_rel_test ;"
            #query = select([table])  #
            print("ici !")
            cursor = conn.execute(querySQL)
            result = cursor.fetchall()
            print(result)
            # print(jsonify(result))

           # result = f"',{result},'",
            data = {}
            i = 0
            for line in result:
                data[i] = str(line)
                i += 1
            print(type(data))
            print(data)
            return data, 200

        except:
            msg = "Get problem, you've done something wrong, or our developers / Work in progress ! Schema not specified or no data"
            print(msg)
            return msg, 400

@api.route("/api/sonde/")
class cSonde(Resource):
    def get(*param):
        '''Retourne les données concernant une sonde'''
        data = api.payload
        print('réception demande données sur une sonde')
        if data is None:
            data = request.get_json()
        if not data:
            data = {"response": "ERROR"}
            return data, 404





def getSonde(pIdSonde, pIpSonde,pTableSonde=tSonde):

    Sonde = Table(pTableSonde, metadata, autoload_with=engine)
    print(Sonde.columns)
    #  req = session.query(Sonde.sonid).filter(Sonde.sonid == int(pIdSonde)).all()
    req = f"SELECT t_sonde.sonid FROM t_sonde WHERE sonid = {int(pIdSonde)};"
    cursor = conn.execute(req)
    result = cursor.fetchall()

    # session.query(Sonde).filter(Sonde.sonid == int(pIdSonde))

    if len(result) == 0:
        req = Sonde.insert().values(sonip=str(pIpSonde))
        conn.execute(req)
        session.commit()
        print("ajout sonde")

        # return IdSonde

    print(f"sonde {pIdSonde} existante")
    return None



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
    app.run(host='0.0.0.0', port='5001', debug=True)
