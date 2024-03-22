from flask_restful import Resource
from flask import request, session

from models.models import Insight
from config import api

class Insights(Resource):
    def get(self):
        list = []

        for insights in Insight.query.all():
            insights_obj = insights.to_dict()
            list.append(insights_obj)

        return list, 200
    
api.add_resource(Insights, "/insights")