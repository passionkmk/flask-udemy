from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):    # Resource get method override
        for item in items:
            if item['name'] == name:
                return item
        return {'item': None}, 404 # Not found error code

    def post(self, name):
        item = {'name': name, 'price': 12.00}
        items.append(item)
        return item, 201 # Created code
    
api.add_resource(Item, '/item/<string:name>')  # http://127.0.0.1:5000/student/Rolf

app.run(port=5000)