from flask import Flask
from flask_restful import Resource, Api
from pymongo import MongoClient

try:
    mongo_client = MongoClient('localhost', 27017)
    db = mongo_client.covid19
    daily_collection = db['daily']
    case_collection = db['case']        # only Singapore now
except Exception as err:
    print("Failed to connect to mongodb")

app = Flask(__name__)
api = Api(app)

class Ping(Resource):
    def get(self):
        return {'pong': True}

api.add_resource(Ping, '/api/ping')

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
