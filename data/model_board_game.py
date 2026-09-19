import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class BoardGame(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'board_games'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    picture = sqlalchemy.Column(sqlalchemy.LargeBinary, nullable=True)
    min_duration = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)   # минуты
    max_duration = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)   # минуты
    min_number_players = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    max_number_players = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)            # возрастное ограничение
    rules = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.Text, nullable=True)

    def __repr__(self):
        return f'<BoardGame> {self.id} {self.name}'