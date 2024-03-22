from flask_restful import Resource
from flask import request, session

from models.models import Action
from config import api

class Actions(Resource):
    def get(self):
        list = []

        for action in Action.query.all():
            action_obj = action.to_dict()
            list.append(action_obj)

        return list, 200
    
api.add_resource(Actions, "/actions")