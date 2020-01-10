from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

adverts = [
    {
        "advertid": 1,
        "keyword": 'network',
        "advert": "Network Engineer Job available in Belfast!"
    },
    {
        "advertid": 2,
        "keyword": 'network',
        "advert": "These are the best networks in the world!"
    },
    {
        "advertid": 3,
        "keyword": 'test',
        "advert": "Testing role available in Belfast IT company!"
    }
]

class Advert(Resource):
    def get(self, name):
        for advert in adverts:
            if(name == advert["keyword"]):
                return advert, 200
        return "User not found", 404
    
class Default(Resource):
    def get(self):
        return "User not found", 404

api.add_resource(Default, "/")
api.add_resource(Advert, "/advert/<string:name>")

app.run(debug=True)
