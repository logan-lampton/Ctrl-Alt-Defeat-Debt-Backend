from flask_restful import Resource
from flask import request, session

from models.models import Personal_goal
from config import api, db

class Personal_goals(Resource):
    def get(self):
        list = []

        for goal in Personal_goal.query.all():
            goal_obj = goal.to_dict()
            list.append(goal_obj)

        return list, 200
    
api.add_resource(Personal_goals, "/personal_goals")