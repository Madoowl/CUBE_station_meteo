from flask import Flask, request
from flask_restplus import Resource, Api
import time

# Config Flask App Definition
app = Flask(__name__)
api = Api(app=app, version="0.1", doc="/api", title="API station météo", description="Test API station météo",
          default="mon api", default_label='ceci est une api de test', validate=True)


# DEMO with simple api function via HTTP GET in default namespace

@api.route("/api/tempRel/")
class cTmpRel(Resource):
    def post(self):
        """
        Add new rel to the DB """
        data = request.get_json()
        if not data:
            data = {"response": "ERROR"}
            return data, 404
        else:  # renvoie des données et insertions dans DB
            tmstmp = time.time()
            title = data.get('title')

            if title:
                if mydb.books.find_one({"title": title}):
                    return {"response": "book already exists."}, 403
                else:
                    mydb.insert(data)
        pass

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

@api.route("/api/v1/time")
class Time(Resource):
    @api.response(200, 'Flask Time : Success')
    @api.response(400, 'Flask DateTime: Error')
    def get(self):
        """
        Renvoi la date actuelle et le timestamp
        """
        current_timestamp = datetime.datetime.now().timestamp()
        current_date = datetime.datetime.now()
        return {'response': {
            'current_date': str(current_date),
            'current_timestamp': str(current_timestamp)}
               }, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
