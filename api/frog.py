from flask import Blueprint, jsonify
from flask_restful import Api, Resource
import random
from model.frog_items import *

frog_item_api = Blueprint('frog_item_api', __name__,
                   url_prefix='/api/frog-items')

api = Api(frog_item_api)

class FrogItemsAPI:
    class _Create(Resource):
        def post(self, item):
            pass
            
    class _Read(Resource):
        def get(self):
            return jsonify(getFrogItems())

    class _ReadID(Resource):
        def get(self, id):
            return jsonify(getFrogItem(id))

    class _ReadRandom(Resource):
        def get(self):
            return jsonify(getRandomFrogItem())
    
    class _ReadCount(Resource):
        def get(self):
            count = countFrogItems()
            countMsg = {'count': count}
            return jsonify(countMsg)

    class _UpdateLike(Resource):
        def put(self, id):
            addFrogItemLike(id)
            return jsonify(getFrogItem(id))

    class _UpdateDislike(Resource):
        def put(self, id):
            addFrogItemDislike(id)
            return jsonify(getFrogItem(id))

    api.add_resource(_Create, '/create/<string:item>')
    api.add_resource(_Read, '/')
    api.add_resource(_ReadID, '/<int:id>')
    api.add_resource(_ReadRandom, '/random')
    api.add_resource(_ReadCount, '/count')
    api.add_resource(_UpdateLike, '/like/<int:id>')
    api.add_resource(_UpdateDislike, '/dislike/<int:id>')

if __name__ == "__main__": 
    server = 'https://flask.nighthawkcodingsociety.com'
    url = server + "/api/frog-items"
    responses = []

    count_response = requests.get(url+"/count")
    count_json = count_response.json()
    count = count_json['count']

    num = str(random.randint(0, count-1))
    responses.append(
        requests.get(url+"/"+num)
    ) 
    responses.append(
        requests.put(url+"/like/"+num)
    ) 
    responses.append(
        requests.put(url+"/dislike/"+num)
    ) 

    responses.append(
        requests.get(url+"/random")
    ) 

    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")
