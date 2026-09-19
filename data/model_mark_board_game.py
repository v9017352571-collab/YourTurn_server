import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class MarkBoardGame(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'mark_board_games'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    board_game_id = sqlalchemy.Column(sqlalchemy.Integer,
                                      sqlalchemy.ForeignKey('board_games.id'), nullable=True)
    creator_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey('users.id'), nullable=True)
    description = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    rating = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)  # 1..5

    def __repr__(self):
        return f'<MarkBoardGame> {self.id} game={self.board_game_id} rating={self.rating}'