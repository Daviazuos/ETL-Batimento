from flask_restful import reqparse, Resource
import RedisServices
import json

parser = reqparse.RequestParser()

parser.add_argument("Carteira")
parser.add_argument("Filedir")
parser.add_argument("KeysNames")
parser.add_argument("StartAt")

Params = {
    "Carteira": "",
    "KeysNames": "",
    "Filedir": "",
    "StartAt": ""
}

class ApiStart(Resource):
    def get(self):
        return Params

    def post(self):
        args = parser.parse_args()
        RedisReturn = RedisServices.SendToReddis(args)
        return RedisReturn, 201
