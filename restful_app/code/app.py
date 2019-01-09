from flask import Flask, request
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
        data = request.get_json() # request가 JSON인지 확인, force=True force를 True로 해두면 application/JSON Header 설정을 하지 않아도 됨 근데 위험
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201 # Created code

class ItemList(Resource):
    def get(self):
        return {'items': items}
    
api.add_resource(Item, '/item/<string:name>')  # http://127.0.0.1:5000/student/Rolf
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)