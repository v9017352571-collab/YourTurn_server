import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class GameGenre(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'game_genres'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    board_game_id = sqlalchemy.Column(sqlalchemy.Integer,
                                      sqlalchemy.ForeignKey('board_games.id'), nullable=False)
    genre_id = sqlalchemy.Column(sqlalchemy.Integer,
                                 sqlalchemy.ForeignKey('genres.id'), nullable=False)

    __table_args__ = (
        sqlalchemy.UniqueConstraint('board_game_id', 'genre_id', name='uq_game_genre'),
    )

    def __repr__(self):
        return f'<GameGenre> game={self.board_game_id} genre={self.genre_id}'