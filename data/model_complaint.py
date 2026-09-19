import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class Complaint(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'complaints'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    from_user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                     sqlalchemy.ForeignKey('users.id'), nullable=True)
    to_user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey('users.id'), nullable=True)
    table_id = sqlalchemy.Column(sqlalchemy.Integer,
                                 sqlalchemy.ForeignKey('game_tables.id'), nullable=True)
    text = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    complaint_category_id = sqlalchemy.Column(sqlalchemy.Integer,
                                              sqlalchemy.ForeignKey('complaints_categories.id'),
                                              nullable=True)

    def __repr__(self):
        return f'<Complaint> {self.id} from={self.from_user_id} to={self.to_user_id}'