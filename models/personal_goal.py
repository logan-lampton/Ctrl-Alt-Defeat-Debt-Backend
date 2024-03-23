from config import db
from sqlalchemy_serializer import SerializerMixin

class Personal_goal(db.Model, SerializerMixin):
    __tablename__ = 'personal_goals'

    serialize_rules = ('-insights.personal_goal', '-user')
    
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String, nullable=False)
    saving_target = db.Column(db.Float, default=0, nullable=False)
    start_timeframe = db.Column(db.DateTime, server_default=db.func.now())
    end_timeframe = db.Column(db.DateTime, nullable=False)
    emoji = db.Column(db.String)
    amount_saved = db.Column(db.Float, default=0)
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    insights = db.relationship("Insight", cascade="all, delete", backref="personal_goal")
    
    def __repr__(self):
        return f"Personal_goal(id={self.id}, " + \
            f"name={self.name}, " + \
            f"saving_target={self.saving_target}, " + \
            f"start_timeframe={self.start_timeframe}, " + \
            f"end_timeframe={self.end_timeframe}, " + \
            f"emoji={self.emoji}, " + \
            f"amount_saved={self.amount_saved}, " + \
            f"user_id={self.user_id}, " + \
            f"insights={self.insights})" 