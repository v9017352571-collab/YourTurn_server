import sqlalchemy as sa
import datetime
from sqlalchemy_serializer import SerializerMixin
from data.db_session import Base

class Message(Base, SerializerMixin):
    __tablename__ = 'messages'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    creator_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=False)
    table_id = sa.Column(sa.Integer, sa.ForeignKey('game_tables.id'), nullable=False)
    creation_time = sa.Column(sa.DateTime, default=datetime.datetime.now)
    encrypted_payload = sa.Column(sa.Text, nullable=False)  # E2EE
    encrypted_picture = sa.Column(sa.LargeBinary, nullable=True)  # E2EE
    status_id = sa.Column(sa.Integer, sa.ForeignKey('message_statuses.id'), nullable=True)