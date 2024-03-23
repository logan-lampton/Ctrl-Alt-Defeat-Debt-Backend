from flask_restful import Resource
from flask import request, session

from models.models import Insight
from config import api, db

class Insights(Resource):
    def get(self):
        list = []

        for insights in Insight.query.all():
            insights_obj = insights.to_dict()
            list.append(insights_obj)

        return list, 200
    
    def post(self):
        user_id = session.get("user_id")
        if not user_id:
            return {"message": "Unauthorized"}, 401
        new_insight = Insight(
           name=request.get_json()["name"],
           savings_monthly=request.get_json()["savings_monthly"],
           savings_needed=request.get_json()["savings_needed"],
           strategy=request.get_json()["strategy"]
        )
        new_insight.goal_id = request.get_json()["goal_id"]
        new_insight.personal_goal_id = request.get_json()["personal_goal_id"]

        db.session.add(new_insight)
        db.session.commit()

        return new_insight.to_dict(), 201
    
    def delete(self):
        id = request.get_json()["id"]
        insight = Insight.query.filter(Insight.id == id).first()

        db.session.delete(insight)
        db.session.commit()

        return {"message": "Group goal successfully deleted"}, 200
    
api.add_resource(Insights, "/insights")