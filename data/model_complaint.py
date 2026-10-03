import sqlalchemy as sa
from sqlalchemy_serializer import SerializerMixin
from data.db_session import Base

class Complaint(Base, SerializerMixin):
    __tablename__ = 'complaints'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    from_user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=True)
    to_user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=True)
    table_id = sa.Column(sa.Integer, sa.ForeignKey('game_tables.id'), nullable=True)
    text = sa.Column(sa.Text, nullable=True)
    complaint_category_id = sa.Column(sa.Integer, sa.ForeignKey('complaints_categories.id'), nullable=True)