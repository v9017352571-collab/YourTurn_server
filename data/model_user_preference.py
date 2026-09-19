import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class UserPreference(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'user_preferences'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey('users.id'), nullable=False, unique=True)
    preferred_min_duration = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)  # минуты
    preferred_max_duration = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)  # минуты
    preferred_min_players = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    preferred_max_players = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    def __repr__(self):
        return f'<UserPreference> {self.id} user={self.user_id}'