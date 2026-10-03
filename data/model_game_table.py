import sqlalchemy as sa
import datetime
from sqlalchemy_serializer import SerializerMixin
from data.db_session import Base

class GameTable(Base, SerializerMixin):
    __tablename__ = 'game_tables'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False)
    creator_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=True)
    creation_time = sa.Column(sa.DateTime, default=datetime.datetime.now)
    location_id = sa.Column(sa.Integer, sa.ForeignKey('locations.id'), nullable=True)
    description = sa.Column(sa.Text, nullable=True)
    min_age = sa.Column(sa.Integer, nullable=True)
    max_age = sa.Column(sa.Integer, nullable=True)