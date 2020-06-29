from flask import Flask
import Controllers
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

api.add_resource(Controllers.ApiStart, '/CreateBatimento', '/CreateBatimento/<ID>')

if __name__ == '__main__':
    app.run(debug=True)