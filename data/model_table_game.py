import sqlalchemy as sa
from sqlalchemy_serializer import SerializerMixin
from data.db_session import Base

class TableGame(Base, SerializerMixin):
    __tablename__ = 'table_games'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    table_id = sa.Column(sa.Integer, sa.ForeignKey('game_tables.id'), nullable=False)
    board_game_id = sa.Column(sa.Integer, sa.ForeignKey('board_games.id'), nullable=False)