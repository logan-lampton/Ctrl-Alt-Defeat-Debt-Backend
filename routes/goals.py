from flask_restful import Resource
from flask import request, session
from datetime import datetime

from models.models import Goal
from config import api, db

class Goals(Resource):
    def get(self):
        list = []

        for goal in Goal.query.all():
            goal_obj = goal.to_dict()
            list.append(goal_obj)

        return list, 200
    
    def post(self):
        user_id = session.get("user_id")
        if not user_id:
            return {"message": "Unauthorized"}, 401
        new_goal = Goal(
           name=request.get_json()["name"],
           saving_target=request.get_json()["saving_target"],
           group_id=request.get_json()["group_id"],
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
    
    def delete(self):
        id = request.get_json()["id"]
        goal = Goal.query.filter(Goal.id == id).first()

        db.session.delete(goal)
        db.session.commit()

        return {"message": "Group goal successfully deleted"}, 200
    
    # def patch(self):
    #     user_id = session.get("user_id")
    #     if not user_id:
    #         return {"message": "Unauthorized"}, 401
        
    #     id = request.get_json()["id"]
    #     goal = Goal.query.filter(Goal.id == id).first()
    #     setattr(goal, "amount_saved", request.get_json()["amount_saved"])
        
    #     db.session.add(goal)
    #     db.session.commit()

    #     return goal.to_dict(), 201
    
api.add_resource(Goals, "/goals")