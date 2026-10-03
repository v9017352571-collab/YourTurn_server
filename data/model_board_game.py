import sqlalchemy as sa
from sqlalchemy_serializer import SerializerMixin
from data.db_session import Base

class BoardGame(Base, SerializerMixin):
    __tablename__ = 'board_games'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False)
    picture = sa.Column(sa.LargeBinary, nullable=True)
    min_duration = sa.Column(sa.Integer, nullable=True)
    max_duration = sa.Column(sa.Integer, nullable=True)
    min_number_players = sa.Column(sa.Integer, nullable=True)
    max_number_players = sa.Column(sa.Integer, nullable=True)
    age = sa.Column(sa.Integer, nullable=True)
    rules = sa.Column(sa.Text, nullable=True)
    description = sa.Column(sa.Text, nullable=True)