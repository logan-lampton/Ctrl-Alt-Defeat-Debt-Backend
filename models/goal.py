from config import db
from sqlalchemy_serializer import SerializerMixin

class Goal(db.Model, SerializerMixin):
    __tablename__ = 'goals'

    serialize_rules = ('-group', '-user', '-insights.goal', '-insights.goal_id')
    
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String, nullable=False)
    saving_target = db.Column(db.Float(2), default=0, nullable=False)
    start_timeframe = db.Column(db.DateTime, server_default=db.func.now())
    end_timeframe = db.Column(db.DateTime, nullable=False)
    emoji = db.Column(db.String)
    amount_saved = db.Column(db.Float(2), default=0)
    
    group_id = db.Column(db.Integer, db.ForeignKey("groups.id"), nullable=False)
    insights = db.relationship("Insight", cascade="all, delete", backref="goal")
    
    def __repr__(self):
        return f"Goal(id={self.id}, " + \
            f"name={self.name}, " + \
            f"saving_target={self.saving_target}, " + \
            f"start_timeframe={self.start_timeframe}, " + \
            f"end_timeframe={self.end_timeframe}, " + \
            f"emoji={self.emoji}, " + \
            f"amount_saved={self.amount_saved}, " + \
            f"group_id={self.group_id}, " + \
            f"insights={self.insights})" 
    
    