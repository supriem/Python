from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {"Suprim": {"age": 24, "gender": "male"},
		"ross": {"age": 70, "gender": "male"}}

class HelloWorld(Resource):
    def get(self, name, test):
        return name[name]
    # def post(self):
    # 	return {"data" : "Posted"}

api.add_resource(HelloWorld, "/helloworld/<string:name>")
    
#api.add_resource(HelloWorld, "/helloworld")


if __name__ == "__main__":
    app.run(debug = True)