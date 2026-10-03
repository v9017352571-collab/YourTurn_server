import sqlalchemy as sa
from sqlalchemy_serializer import SerializerMixin
from data.db_session import Base

class UserPreference(Base, SerializerMixin):
    __tablename__ = 'user_preferences'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=False, unique=True)
    preferred_min_duration = sa.Column(sa.Integer, nullable=True)
    preferred_max_duration = sa.Column(sa.Integer, nullable=True)
    preferred_min_players = sa.Column(sa.Integer, nullable=True)
    preferred_max_players = sa.Column(sa.Integer, nullable=True)