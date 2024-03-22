from config import db
from sqlalchemy_serializer import SerializerMixin

class Group(db.Model, SerializerMixin):
    __tablename__ = "groups"

    serialize_rules = ('-users.group', '-users.group_id', '-users.personal_goals', '-goals.group', '-goals.group_id', '-goals.insights')

    id = db.Column(db.Integer, primary_key=True)

    is_family = db.Column(db.Boolean, nullable=False)
    name = db.Column(db.String)
    total_income = db.Column(db.String)
    total_expenses = db.Column(db.String)
    _access_token = db.Column(db.String)

    users = db.relationship("User", cascade="all, delete", backref="group")
    goals = db.relationship("Goal", cascade="all, delete", backref="group")
    
    def __repr__(self):
        return f"Group(id={self.id}, " + \
            f"is_family={self.is_family}, " + \
            f"name={self.name}, " + \
            f"name={self._access_token}, " + \
            f"users={self.users}, " + \
            f"goals={self.goals})"