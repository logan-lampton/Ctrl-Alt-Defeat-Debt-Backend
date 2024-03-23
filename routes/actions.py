from flask_restful import Resource
from flask import request, session

from models.models import Action
from config import api, db

class Actions(Resource):
    def get(self):
        list = []

        for action in Action.query.all():
            action_obj = action.to_dict()
            list.append(action_obj)

        return list, 200
    
    def post(self):
        user_id = session.get("user_id")
        if not user_id:
            return {"message": "Unauthorized"}, 401
        new_action = Action(
           text=request.get_json()["text"],
        )
        new_action.insight_id = request.get_json()["insight_id"]

        db.session.add(new_action)
        db.session.commit()

        return new_action.to_dict(), 201
    
    def delete(self):
        id = request.get_json()["id"]
        action = Action.query.filter(Action.id == id).first()

        db.session.delete(action)
        db.session.commit()

        return {"message": "Group goal successfully deleted"}, 200
    
api.add_resource(Actions, "/actions")