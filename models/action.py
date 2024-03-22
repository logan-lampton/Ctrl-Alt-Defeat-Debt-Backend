from config import db
from sqlalchemy_serializer import SerializerMixin

class Action(db.Model, SerializerMixin):
    __tablename__ = "actions"

    serialize_rules = ()

    id = db.Column(db.Integer, primary_key=True)

    text = db.Column(db.String)
    
    insight_id = db.Column(db.Integer, db.ForeignKey("insights.id"))
    
    def __repr__(self):
        return f"Actions(id={self.id}, " + \
            f"text={self.text}, " + \
            f"insight_id={self.insight_id}) "