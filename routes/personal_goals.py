from flask_restful import Resource
from flask import request, session
from datetime import datetime

from models.models import Personal_goal
from config import api, db

class Personal_goals(Resource):
    def get(self):
        list = []

        for goal in Personal_goal.query.all():
            goal_obj = goal.to_dict()
            list.append(goal_obj)

        return list, 200
    

    def post(self):
        user_id = session.get("user_id")
        if not user_id:
            return {"message": "Unauthorized"}, 401
        new_personal_goal = Personal_goal(
            user_id =request.get_json()["user_id"],
            name=request.get_json()["name"],
            saving_target=request.get_json()["saving_target"],
            emoji=request.get_json()["emoji"],
        )
        #logic for converting string datetime in python object
        end_timeframe_str = request.get_json()["end_timeframe"]
        year = int(end_timeframe_str[0:4])
        month = int(end_timeframe_str[5:7])
        day = int(end_timeframe_str[8:10])
        end_timeframe = datetime(year, month, day)

        new_personal_goal.end_timeframe = end_timeframe
        
        db.session.add(new_personal_goal)
        db.session.commit()
        

        return new_personal_goal.to_dict(), 201

    def delete(self):
        id = request.get_json()["id"]
        personal_goal = Personal_goal.query.filter(Personal_goal.id == id).first()

        db.session.delete(personal_goal)
        db.session.commit()

        return {"message": "Personal goal successfully deleted"}, 200
    
    def patch(self):
        user_id = session.get("user_id")
        if not user_id:
            return {"message": "Unauthorized"}, 401
        new_goal = Personal_goal(
           name=request.get_json()["name"],
           saving_target=request.get_json()["saving_target"],
           user_id=request.get_json()["user_id"],
           emoji=request.get_json()["emoji"],
        )

        #logic for converting string datetime in python object
        end_timeframe_str = request.get_json()["end_timeframe"]
        year = int(end_timeframe_str[0:4])
        month = int(end_timeframe_str[5:7])
        day = int(end_timeframe_str[8:10])
        end_timeframe = datetime(year, month, day)

        new_goal.end_timeframe = end_timeframe

        db.session.add(new_goal)
        db.session.commit()

        return new_goal.to_dict(), 201
    
api.add_resource(Personal_goals, "/personal_goals")