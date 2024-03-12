from config import db
from sqlalchemy_serializer import SerializerMixin

class Account(db.Model, SerializerMixin):
    __tablename__ = "accounts"
    
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    balance = db.Column(db.Float, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return f'Account(id={self.id}, ' + \
            f'name={self.name}, ' + \
            f'type={self.type}, ' + \
            f'balance={self.balance}, ' + \
            f'user_id={self.user_id})'