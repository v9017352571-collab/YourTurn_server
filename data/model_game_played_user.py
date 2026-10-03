import sqlalchemy as sa
from sqlalchemy_serializer import SerializerMixin
from data.db_session import Base

class GamePlayedUser(Base, SerializerMixin):
    __tablename__ = 'game_played_users'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    game_played_id = sa.Column(sa.Integer, sa.ForeignKey('games_played.id'), nullable=False)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=False)