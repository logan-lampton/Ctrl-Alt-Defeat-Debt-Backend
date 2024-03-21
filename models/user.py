from config import db, bcrypt
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property

class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    serialize_rules = ('-group', '-goal', '-personal_goals.insights', '-personal_goals.user', '-personal_goals.user_id', '-insights')

    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    phone = db.Column(db.String, unique=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    admin = db.Column(db.Boolean, default=True, nullable=False)
    visibility_status = db.Column(db.String, default="Full",nullable=False)
    rent = db.Column(db.Float, nullable=False)
    income = db.Column(db.Float, default=0, nullable=False)

    _password_hash = db.Column(db.String, nullable=False)
    _access_token = db.Column(db.String)
    _totp_secret = db.Column(db.String)

    group_id = db.Column(db.Integer, db.ForeignKey("groups.id"))
    personal_goals = db.relationship("Personal_goal", cascade="all, delete", backref="user")

    @hybrid_property
    def password_hash(self):
        raise AttributeError

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))
    
    def __repr__(self):
        return f"User(id={self.id}, " + \
            f"first_name={self.first_name}, " + \
            f"last_name={self.last_name}, " + \
            f"email={self.email}, " + \
            f"phone={self.phone}, " + \
            f"created_at={self.created_at}, " + \
            f"admin={self.admin}, " + \
            f"visibility_status={self.visibility_status}, " + \
            f"rent={self.rent}, " + \
            f"income={self.income}, " + \
            f"_access_token={self._access_token}, " + \
            f"_totp_secret={self._totp_secret}, " + \
            f"group_id={self.group_id})"