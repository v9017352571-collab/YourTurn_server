import sqlalchemy as sa
import datetime
from sqlalchemy_serializer import SerializerMixin
from data.db_session import Base

class TablePlayer(Base, SerializerMixin):
    __tablename__ = 'table_players'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    table_id = sa.Column(sa.Integer, sa.ForeignKey('game_tables.id'), nullable=False)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=False)
    joined_at = sa.Column(sa.DateTime, default=datetime.datetime.now)
    role = sa.Column(sa.String, default='player')