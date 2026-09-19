import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class GamesPlayed(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'games_played'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    table_id = sqlalchemy.Column(sqlalchemy.Integer,
                                 sqlalchemy.ForeignKey('game_tables.id'), nullable=True)
    board_game_id = sqlalchemy.Column(sqlalchemy.Integer,
                                      sqlalchemy.ForeignKey('board_games.id'), nullable=True)
    duration = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)  # минуты
    winner_id = sqlalchemy.Column(sqlalchemy.Integer,
                                  sqlalchemy.ForeignKey('users.id'), nullable=True)
    description = sqlalchemy.Column(sqlalchemy.Text, nullable=True)

    def __repr__(self):
        return f'<GamesPlayed> {self.id} table={self.table_id}'