import sqlalchemy as sa
from sqlalchemy_serializer import SerializerMixin
from data.db_session import Base

class UserDislikedGame(Base, SerializerMixin):
    __tablename__ = 'user_disliked_games'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=False)
    board_game_id = sa.Column(sa.Integer, sa.ForeignKey('board_games.id'), nullable=False)
    __table_args__ = (sa.UniqueConstraint('user_id', 'board_game_id', name='uq_user_disliked_game'),)