from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
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
        return {'pong': True, 'version': 1}


class CountryResource(Resource):
    def get(self):
        return {
            'Singapore': {
                'short': 'SG',
                'area': 724,
                'population': 5994300,
                'capital': 'Singapore',
                'name_cn': '新加坡'
            },
            'Brunei': {
                'short': 'BN',
                'area': 5765,
                'population': 440920,
                'capital': 'Seri Begawan',
                'name_cn': '文莱'
            },
            'Cambodia': {
                'short': 'KH',
                'area': 181035,
                'populartion': 16718965,
                'capital': 'Phnom Penh',
                'name_cn': '柬埔寨'
            },
            'East Timor': {
                'short': 'TL',
                'area': 14874,
                'population': 1267974,
                'capital': 'Dili',
                'name_cn': '东帝汶'
            },
            'Indonesia': {
                'short': 'ID',
                'area': 1904569,
                'population': 267670543,
                'capital': 'Jakarta',
                'name_cn': '印尼'
            },
            'Laos': {
                'short': 'LA',
                'area': 236800,
                'population': 7061507,
                'capital': 'Vientiane',
                'name_cn': '老挝'
            },
            'Malaysia': {
                'short': 'MY',
                'area': 329847,
                'population': 31528033,
                'capital': 'Kuala Lumpur',
                'name_cn': '马来西亚'
            },
            'Myanmar': {
                'short': 'MM',
                'area': 676578,
                'population': 53708320,
                'capital': 'Nay Pyi Taw',
                'name_cn': '缅甸'
            },
            'Philippines': {
                'short': 'PH',
                'area': 300000,
                'population': 106651394,
                'capital': 'Manila',
                'name_cn': '菲律宾'
            },
            'Thailand': {
                'short': 'TH',
                'area': 513120,
                'population': 69428453,
                'capital': 'Bangkok',
                'name_cn': '泰国'
            },
            'Vietnam': {
                'short': 'VN',
                'area': 33121,
                'population': 95545962,
                'capital': 'Hanoi',
                'name_cn': '越南'
            },
        }


def abort_if_country_doesnt_exist(country_name):
    record = daily_collection.find_one({'country': country_name})
    if not record:
        abort(404, message="Country {} doesn't exist".format(country_name))


class DailyResource(Resource):
    def get(self, country_name):
        parser = reqparse.RequestParser()
        parser.add_argument('limit', type=int)
        parser.add_argument('sort', type=int, default=-1)
        args = parser.parse_args()

        country_name = country_name.capitalize()
        abort_if_country_doesnt_exist(country_name)
        print(args)
        if 'limit' in args and args['limit']:
            records = daily_collection.find({'country': country_name}, {'_id': 0}).sort([('date', args['sort'])])\
                .limit(args['limit'])
        else:
            records = daily_collection.find({'country': country_name}, {'_id': 0}).sort([('date', args['sort'])])
        return list(records)

    """
    def put(self, country_name):
        parser = reqparse.RequestParser()
        args = parser.parse_args()
        # task = {'task': args['task']}
        # TODOS[todo_id] = task
        # return task, 201
    """

class CaseResource(Resource):
    def get(self, country_name):
        parser = reqparse.RequestParser()
        parser.add_argument('limit', type=int)
        parser.add_argument('sort', type=int, default=-1)
        args = parser.parse_args()

        country_name = country_name.capitalize()
        abort_if_country_doesnt_exist(country_name)
        if 'limit' in args and args['limit']:
            records = case_collection.find({'country': country_name}, {'_id': 0}).sort([('date', args['sort'])])\
                .limit(args['limit'])
        else:
            records = case_collection.find({'country': country_name}, {'_id': 0}).sort([('date', args['sort'])])
        return list(records)


api.add_resource(Ping, '/api/ping')
api.add_resource(CountryResource, '/api/countries')
api.add_resource(DailyResource, '/api/daily/<country_name>')
api.add_resource(CaseResource, '/api/case/<country_name>')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
