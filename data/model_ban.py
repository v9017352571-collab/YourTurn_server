import sqlalchemy
import datetime
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class Ban(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'bans'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey('users.id'), nullable=True)
    banned = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    reason = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    started_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    until = sqlalchemy.Column(sqlalchemy.DateTime, nullable=True)

    def __repr__(self):
        return f'<Ban> {self.id} user={self.user_id} banned={self.banned}'