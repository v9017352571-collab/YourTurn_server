import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class MessageStatus(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'message_statuses'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True)  # sent/delivered/read

    def __repr__(self):
        return f'<MessageStatus> {self.id} {self.name}'