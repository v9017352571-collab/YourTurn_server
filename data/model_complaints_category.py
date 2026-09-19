import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class ComplaintsCategory(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'complaints_categories'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name_complaint = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True)

    def __repr__(self):
        return f'<ComplaintsCategory> {self.id} {self.name_complaint}'