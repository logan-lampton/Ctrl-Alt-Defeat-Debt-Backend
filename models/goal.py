from config import db
from sqlalchemy_serializer import SerializerMixin

class Goal(db.Model, SerializerMixin):
    __tablename__ = 'goals'
    
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String, nullable=False)
    saving_target = db.Column(db.Float, default=0.0, nullable=False)
    start_timeframe = db.Column(db.DateTime, server_default=db.func.now())
    end_timeframe = db.Column(db.DateTime)
    emoji = db.Column(db.String)
    
    group_id = db.Column(db.Integer, db.ForeignKey("groups.id"), nullable=False)
    
    def __repr__(self):
        return f"Goal(id={self.id}, " + \
            f"name={self.name}, " + \
            f"saving_target={self.saving_target}, " + \
            f"start_timeframe={self.start_time}, " + \
            f"end_timeframe={self.end_time}, " + \
            f"emoji={self.emoji}, " + \
            f"group_id={self.group_id})" 
    
    