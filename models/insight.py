from config import db
from sqlalchemy_serializer import SerializerMixin

class Insight(db.Model, SerializerMixin):
    __tablename__ = "insights"

    serialize_rules = ('-goal', '-personal_goal', '-actions.insight')

    id = db.Column(db.Integer, primary_key=True)

    savings_monthly = db.Column(db.Float(2))
    savings_needed = db.Column(db.Float(2))
    strategy = db.Column(db.String)

    goal_id = db.Column(db.Integer, db.ForeignKey("goals.id"))
    personal_goal_id = db.Column(db.Integer, db.ForeignKey("personal_goals.id"))
    actions = db.relationship("Action", cascade="all, delete", backref="insight")
    
    def __repr__(self):
        return f"Insight(id={self.id}, " + \
            f"savings_monthly={self.savings_monthly}, " + \
            f"savings_needed={self.savings_needed}, " + \
            f"strategy={self.strategy}, " + \
            f"actions={self.actions}, " + \
            f"group_id={self.goal_id}) "