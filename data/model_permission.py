import sqlalchemy as sa
from sqlalchemy_serializer import SerializerMixin
from data.db_session import Base

class Permission(Base, SerializerMixin):
    __tablename__ = 'permissions'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name_permission = sa.Column(sa.String, nullable=False, unique=True)