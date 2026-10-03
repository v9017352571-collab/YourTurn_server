import sqlalchemy as sa
from sqlalchemy_serializer import SerializerMixin
from data.db_session import Base

class UserPreferredGenre(Base, SerializerMixin):
    __tablename__ = 'user_preferred_genres'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    user_preference_id = sa.Column(sa.Integer, sa.ForeignKey('user_preferences.id'), nullable=False)
    genre_id = sa.Column(sa.Integer, sa.ForeignKey('genres.id'), nullable=False)
    __table_args__ = (sa.UniqueConstraint('user_preference_id', 'genre_id', name='uq_user_preferred_genre'),)