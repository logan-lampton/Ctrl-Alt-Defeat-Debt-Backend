from config import db, bcrypt
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property

class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    _password_hash = db.Column(db.String, nullable=False)

    groups = db.relationship("Group", backref="user")
    accounts =db.relationship("Account", backref="user")

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
            f"username={self.username}, " + \
            f"email={self.email}, " + \
            f"phone={self.phone}, " + \
            f"created_at={self.created_at})"