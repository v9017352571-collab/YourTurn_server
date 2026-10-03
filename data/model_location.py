import sqlalchemy as sa
from sqlalchemy_serializer import SerializerMixin
from data.db_session import Base

class Location(Base, SerializerMixin):
    __tablename__ = 'locations'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    address = sa.Column(sa.String, nullable=True)
    latitude = sa.Column(sa.Float, nullable=True)
    longitude = sa.Column(sa.Float, nullable=True)