import sqlalchemy
import datetime
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash
from data.db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    about_me = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    creation_time = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=True)
    phone = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    tg_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    avatar = sqlalchemy.Column(sqlalchemy.LargeBinary, nullable=True)
    rating = sqlalchemy.Column(sqlalchemy.Float, default=0.0)

    # --- НОВОЕ ПОЛЕ ДЛЯ E2EE ---
    public_key = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # Base64 строка публичного ключа

    location_id = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey('locations.id'), nullable=True)
    permission_id = sqlalchemy.Column(sqlalchemy.Integer,
                                      sqlalchemy.ForeignKey('permissions.id'), nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def __repr__(self):
        return f'<User> {self.id} {self.name}'

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)