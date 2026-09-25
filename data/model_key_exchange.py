import sqlalchemy
import datetime
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class KeyExchange(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'key_exchanges'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    recipient_id = sqlalchemy.Column(sqlalchemy.Integer,
                                     sqlalchemy.ForeignKey('users.id'), nullable=False)
    sender_id = sqlalchemy.Column(sqlalchemy.Integer,
                                  sqlalchemy.ForeignKey('users.id'), nullable=False)

    # Эфемерный публичный ключ отправителя (Base64)
    ephemeral_public_key = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    # Личный Sender Key отправителя, зашифрованный общим секретом (Base64)
    encrypted_sender_key = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    # Флаг: забрал ли уже получатель этот ключ (чтобы очистить мусор)
    is_consumed = sqlalchemy.Column(sqlalchemy.Boolean, default=False)

    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return f'<KeyExchange> {self.id} from={self.sender_id} to={self.recipient_id} consumed={self.is_consumed}'