import sqlalchemy
import datetime
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class GameTable(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'game_tables'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    creator_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey('users.id'), nullable=True)
    creation_time = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    location_id = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey('locations.id'), nullable=True)
    description = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    min_age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    max_age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    def __repr__(self):
        return f'<GameTable> {self.id} {self.name}'