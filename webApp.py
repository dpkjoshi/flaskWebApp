from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


# @app.route("/")
# def hello():
#     return "Hello  World!"

class HelloWorld(Resource):
    @staticmethod
    def get():
        return {'about': 'Hello World!'}

    def put(self):
        some_json = request.json
        return {"data": some_json}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
