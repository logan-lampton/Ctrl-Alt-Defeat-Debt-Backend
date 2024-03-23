from config import db
from sqlalchemy_serializer import SerializerMixin

class Insight(db.Model, SerializerMixin):
    __tablename__ = "insights"

    serialize_rules = ('-goal', '-personal_goal', '-actions.insight')

    id = db.Column(db.Integer, primary_key=True)

    savings_monthly = db.Column(db.Float(2), nullable=False)
    savings_needed = db.Column(db.Float(2), nullable=False)
    strategy = db.Column(db.String, nullable=False)

    goal_id = db.Column(db.Integer, db.ForeignKey("goals.id"))
    personal_goal_id = db.Column(db.Integer, db.ForeignKey("personal_goals.id"))
    actions = db.relationship("Action", cascade="all, delete", backref="insight")
    
    def __repr__(self):
        return f"Insight(id={self.id}, " + \
            f"savings_monthly={self.savings_monthly}, " + \
            f"savings_needed={self.savings_needed}, " + \
            f"strategy={self.strategy}, " + \
            f"goal_id={self.goal_id}, " + \
            f"personal_goal_id={self.personal_goal_id}, " + \
            f"actions={self.actions}) "