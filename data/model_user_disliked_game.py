import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class UserDislikedGame(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'user_disliked_games'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey('users.id'), nullable=False)
    board_game_id = sqlalchemy.Column(sqlalchemy.Integer,
                                      sqlalchemy.ForeignKey('board_games.id'), nullable=False)

    __table_args__ = (
        sqlalchemy.UniqueConstraint('user_id', 'board_game_id', name='uq_user_disliked_game'),
    )

    def __repr__(self):
        return f'<UserDislikedGame> user={self.user_id} game={self.board_game_id}'