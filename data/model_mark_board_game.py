import sqlalchemy as sa
from sqlalchemy_serializer import SerializerMixin
from data.db_session import Base

class MarkBoardGame(Base, SerializerMixin):
    __tablename__ = 'mark_board_games'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    board_game_id = sa.Column(sa.Integer, sa.ForeignKey('board_games.id'), nullable=True)
    creator_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=True)
    description = sa.Column(sa.Text, nullable=True)
    rating = sa.Column(sa.Integer, nullable=True)