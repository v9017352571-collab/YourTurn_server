import sqlalchemy as sa
from sqlalchemy_serializer import SerializerMixin
from data.db_session import Base

class GamesPlayed(Base, SerializerMixin):
    __tablename__ = 'games_played'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    table_id = sa.Column(sa.Integer, sa.ForeignKey('game_tables.id'), nullable=True)
    board_game_id = sa.Column(sa.Integer, sa.ForeignKey('board_games.id'), nullable=True)
    duration = sa.Column(sa.Integer, nullable=True)
    winner_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=True)
    description = sa.Column(sa.Text, nullable=True)