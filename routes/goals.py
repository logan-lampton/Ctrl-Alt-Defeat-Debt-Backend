from flask_restful import Resource
from flask import request, session

from models.models import Goal
from config import api, db

class Goals(Resource):
    def get(self):
        list = []

        for goal in Goal.query.all():
            goal_obj = goal.to_dict()
            list.append(goal_obj)

        return list, 200
    
api.add_resource(Goals, "/goals")