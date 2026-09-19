import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class UserPreferredGenre(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'user_preferred_genres'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_preference_id = sqlalchemy.Column(sqlalchemy.Integer,
                                           sqlalchemy.ForeignKey('user_preferences.id'),
                                           nullable=False)
    genre_id = sqlalchemy.Column(sqlalchemy.Integer,
                                 sqlalchemy.ForeignKey('genres.id'), nullable=False)

    __table_args__ = (
        sqlalchemy.UniqueConstraint('user_preference_id', 'genre_id',
                                    name='uq_user_preferred_genre'),
    )

    def __repr__(self):
        return f'<UserPreferredGenre> pref={self.user_preference_id} genre={self.genre_id}'