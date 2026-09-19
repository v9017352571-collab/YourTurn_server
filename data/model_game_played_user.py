import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class GamePlayedUser(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'game_played_users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    game_played_id = sqlalchemy.Column(sqlalchemy.Integer,
                                       sqlalchemy.ForeignKey('games_played.id'), nullable=False)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<GamePlayedUser> game={self.game_played_id} user={self.user_id}'