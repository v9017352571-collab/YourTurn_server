import sqlalchemy
import datetime
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class TablePlayer(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'table_players'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    table_id = sqlalchemy.Column(sqlalchemy.Integer,
                                 sqlalchemy.ForeignKey('game_tables.id'), nullable=False)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey('users.id'), nullable=False)
    joined_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    role = sqlalchemy.Column(sqlalchemy.String, default='player')  # host/player

    def __repr__(self):
        return f'<TablePlayer> table={self.table_id} user={self.user_id} role={self.role}'