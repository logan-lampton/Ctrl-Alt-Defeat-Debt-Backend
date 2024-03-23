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
    
    def post(self):
        user_id = session.get("user_id")
        if not user_id:
            return {"message": "Unauthorized"}, 401
        new_personal_goal = Personal_goal(
           name=request.get_json()["name"],
           saving_target=request.get_json()["saving_target"],
           end_timeframe=request.get_json()["end_timeframe"],
        )
        new_personal_goal.user_id = user_id

        db.session.add(new_personal_goal)
        db.session.commit()

        return new_personal_goal.to_dict(), 201
    
    def delete(self):
        id = request.get_json()["id"]
        personal_goal = Personal_goal.query.filter(Personal_goal.id == id).first()

        db.session.delete(personal_goal)
        db.session.commit()

        return {"message": "Personal goal successfully deleted"}, 200
    
    # def patch(self):
    #     user_id = session.get("user_id")
    #     if not user_id:
    #         return {"message": "Unauthorized"}, 401
        
    #     id = request.get_json()["id"]
    #     personal_goal = Personal_goal.query.filter(Personal_goal.id == id).first()
    #     setattr(personal_goal, "amount_saved", request.get_json()["amount_saved"])
        
    #     db.session.add(personal_goal)
    #     db.session.commit()

    #     return personal_goal.to_dict(), 201
    
api.add_resource(Personal_goals, "/personal_goals")