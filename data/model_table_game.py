import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class TableGame(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'table_games'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    table_id = sqlalchemy.Column(sqlalchemy.Integer,
                                 sqlalchemy.ForeignKey('game_tables.id'), nullable=False)
    board_game_id = sqlalchemy.Column(sqlalchemy.Integer,
                                      sqlalchemy.ForeignKey('board_games.id'), nullable=False)

    def __repr__(self):
        return f'<TableGame> table={self.table_id} game={self.board_game_id}'