import sqlalchemy
import datetime
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class Message(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'messages'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    # E2EE: Сервер видит только ID отправителя и получателя (стола), но не содержание
    creator_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey('users.id'), nullable=False)
    table_id = sqlalchemy.Column(sqlalchemy.Integer,
                                 sqlalchemy.ForeignKey('game_tables.id'), nullable=False)

    creation_time = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)

    # --- E2EE ПОЛЯ ---
    encrypted_payload = sqlalchemy.Column(sqlalchemy.Text, nullable=False)  # Зашифрованный текст (Base64)
    encrypted_picture = sqlalchemy.Column(sqlalchemy.LargeBinary,
                                          nullable=True)  # Зашифрованное изображение (опционально)

    status_id = sqlalchemy.Column(sqlalchemy.Integer,
                                  sqlalchemy.ForeignKey('message_statuses.id'), nullable=True)

    def __repr__(self):
        return f'<Message> {self.id} table={self.table_id} sender={self.creator_id}'