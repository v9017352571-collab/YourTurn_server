import sqlalchemy as sa
import datetime
from sqlalchemy_serializer import SerializerMixin
from data.db_session import Base

class FriendRequest(Base, SerializerMixin):
    __tablename__ = 'friend_requests'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    from_user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=True)
    to_user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=True)
    status = sa.Column(sa.String, default='pending')
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.now)