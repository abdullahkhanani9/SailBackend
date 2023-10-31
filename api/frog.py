from flask import Blueprint, jsonify
from flask_restful import Api, Resource
from __init__ import db
from model.frogs import FrogSpecies  # Make sure this import is correct

frog_item_api = Blueprint('frog_item_api', __name__, url_prefix='/api/frog-items')

api = Api(frog_item_api)

# Rest of your code remains the same
class FrogAPI:
    class _Read(Resource):
        def get(self):
            frogs = FrogSpecies.query.all()
            json_ready = [frog.to_dict() for frog in frogs]
            return jsonify(json_ready)
    api.add_resource(_Read, '/')
