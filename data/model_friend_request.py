import sqlalchemy
import datetime
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class FriendRequest(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'friend_requests'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    from_user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                     sqlalchemy.ForeignKey('users.id'), nullable=True)
    to_user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey('users.id'), nullable=True)
    status = sqlalchemy.Column(sqlalchemy.String, default='pending')  # pending/accepted/rejected
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return f'<FriendRequest> {self.id} from={self.from_user_id} to={self.to_user_id}'