import sqlalchemy as sa
import datetime
from sqlalchemy_serializer import SerializerMixin
from data.db_session import Base

class Ban(Base, SerializerMixin):
    __tablename__ = 'bans'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=True)
    banned = sa.Column(sa.Boolean, default=False)
    reason = sa.Column(sa.Text, nullable=True)
    started_at = sa.Column(sa.DateTime, default=datetime.datetime.now)
    until = sa.Column(sa.DateTime, nullable=True)