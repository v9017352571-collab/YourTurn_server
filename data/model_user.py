import sqlalchemy as sa
import datetime
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash
from data.db_session import Base

class User(Base, UserMixin, SerializerMixin):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=True)
    about_me = sa.Column(sa.Text, nullable=True)
    age = sa.Column(sa.Integer, nullable=True)
    creation_time = sa.Column(sa.DateTime, default=datetime.datetime.now)
    email = sa.Column(sa.String, unique=True, nullable=True)
    phone = sa.Column(sa.String, nullable=True)
    tg_name = sa.Column(sa.String, nullable=True)
    avatar = sa.Column(sa.LargeBinary, nullable=True)
    rating = sa.Column(sa.Float, default=0.0)
    public_key = sa.Column(sa.String, nullable=True)  # E2EE
    location_id = sa.Column(sa.Integer, sa.ForeignKey('locations.id'), nullable=True)
    permission_id = sa.Column(sa.Integer, sa.ForeignKey('permissions.id'), nullable=True)
    hashed_password = sa.Column(sa.String, nullable=True)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)