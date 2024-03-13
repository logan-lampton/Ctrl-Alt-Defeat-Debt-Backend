from flask_restful import Resource
from flask import request, session

from models.models import Group
from config import api, db

class Groups(Resource):
    def get(self):
        list = []

        for group in Group.query.all():
            group_obj = group.to_dict()
            list.append(group_obj)

        return list, 200
    
api.add_resource(Groups, "/groups")