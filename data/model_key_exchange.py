import sqlalchemy as sa
import datetime
from sqlalchemy_serializer import SerializerMixin
from data.db_session import Base

class KeyExchange(Base, SerializerMixin):
    __tablename__ = 'key_exchanges'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    recipient_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=False)
    sender_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=False)
    ephemeral_public_key = sa.Column(sa.String, nullable=False)
    encrypted_sender_key = sa.Column(sa.String, nullable=False)
    is_consumed = sa.Column(sa.Boolean, default=False)
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.now)