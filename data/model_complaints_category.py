import sqlalchemy as sa
from sqlalchemy_serializer import SerializerMixin
from data.db_session import Base

class ComplaintsCategory(Base, SerializerMixin):
    __tablename__ = 'complaints_categories'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name_complaint = sa.Column(sa.String, nullable=False, unique=True)