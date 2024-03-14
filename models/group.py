from config import db
from sqlalchemy_serializer import SerializerMixin

class Group(db.Model, SerializerMixin):
    __tablename__ = "groups"

    serialize_rules = ('-goals.group', '-user')

    id = db.Column(db.Integer, primary_key=True)

    is_family = db.Column(db.Boolean, nullable=False)
    name = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)
    visibility_status = db.Column(db.String, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    goals = db.relationship("Goal", cascade="all, delete", backref="group")
    
    def __repr__(self):
        return f"Group(id={self.id}, " + \
            f"is_family={self.is_family}, " + \
            f"name={self.name}, " + \
            f"role={self.role}, " + \
            f"visibility_status={self.visibility_status}, " + \
            f"user_id={self.user_id})"