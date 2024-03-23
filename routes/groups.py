from flask_restful import Resource
from flask import request, session

from models.models import Group, User
from config import api, db

class Groups(Resource):
    def get(self):
        list = []

        for group in Group.query.all():
            group_obj = group.to_dict()
            list.append(group_obj)

        return list, 200

    def post(self):
        user_id = session.get("user_id")
        user = User.query.filter(User.id == user_id).first()
        if not user_id:
            return {"message": "Unauthorized"}, 401
        new_group = Group(
           name=request.get_json()["name"],
        )
        new_group._access_token = user._access_token
        db.session.add(new_group)
        db.session.commit()

        return new_group.to_dict(), 201
    
    def delete(self):
        id = request.get_json()["id"]
        group = Group.query.filter(Group.id == id).first()

        db.session.delete(group)
        db.session.commit()

        return {"message": "Group goal successfully deleted"}, 200
    
    # def patch(self):
    #     user_id = session.get("user_id")
    #     if not user_id:
    #         return {"message": "Unauthorized"}, 401
        
    #     id = request.get_json()["id"]
    #     group = Group.query.filter(Group.id == id).first()
    #     setattr(group, "name", request.get_json()["name"])
        
    #     db.session.add(group)
    #     db.session.commit()

    #     return group.to_dict(), 201
    
api.add_resource(Groups, "/groups")