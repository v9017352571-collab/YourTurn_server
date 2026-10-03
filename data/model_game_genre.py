import sqlalchemy as sa
from sqlalchemy_serializer import SerializerMixin
from data.db_session import Base

class GameGenre(Base, SerializerMixin):
    __tablename__ = 'game_genres'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    board_game_id = sa.Column(sa.Integer, sa.ForeignKey('board_games.id'), nullable=False)
    genre_id = sa.Column(sa.Integer, sa.ForeignKey('genres.id'), nullable=False)
    __table_args__ = (sa.UniqueConstraint('board_game_id', 'genre_id', name='uq_game_genre'),)