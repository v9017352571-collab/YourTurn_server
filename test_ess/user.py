import sys
import time
import base64
import requests
import threading
from cryptography.hazmat.primitives.asymmetric import x25519
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDFExpand
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

BASE_URL = "http://127.0.0.1:5000"
MY_NAME = input('Your name:')

print(f"\n[{MY_NAME}] Запуск клиента...")

# 1. ГЕНЕРАЦИЯ КЛЮЧЕЙ
my_1on1_priv = x25519.X25519PrivateKey.generate()
my_1on1_pub = my_1on1_priv.public_key()
my_1on1_pub_bytes = my_1on1_pub.public_bytes(
    serialization.Encoding.Raw, serialization.PublicFormat.Raw
)

my_sender_key = Fernet.generate_key()
my_fernet = Fernet(my_sender_key)

print(f"[{MY_NAME}] Регистрация на сервере...")
requests.post(f"{BASE_URL}/register", json={
    "username": MY_NAME,
    "pub_key": base64.b64encode(my_1on1_pub_bytes).decode()
})

# Состояние клиента
peers_sender_keys = {}  # { "peer_name": Fernet_object }
known_peers = set()  # Пир, которым мы УЖЕ отправили свой ключ
known_messages_count = 0


# ==========================================
# ФОНОВЫЙ ПРОЦЕСС 1: ПОСТОЯННЫЙ ОБМЕН КЛЮЧАМИ
# ==========================================
def key_exchange_loop():
    while True:
        try:
            # 1. Забираем НОВЫЕ зашифрованные Sender Keys из ящика
            my_encrypted_keys = requests.get(f"{BASE_URL}/pop_my_sender_keys?username={MY_NAME}").json()
            for item in my_encrypted_keys:
                sender_name = item['sender']
                eph_pub_bytes = base64.b64decode(item['eph_pub'])
                enc_key_bytes = base64.b64decode(item['enc_key'])

                eph_pub_key = x25519.X25519PublicKey.from_public_bytes(eph_pub_bytes)
                shared_secret = my_1on1_priv.exchange(eph_pub_key)
                hkdf = HKDFExpand(algorithm=hashes.SHA256(), length=32, info=b"group-setup")
                wrap_key = base64.urlsafe_b64encode(hkdf.derive(shared_secret))

                temp_fernet = Fernet(wrap_key)
                peer_sender_key = temp_fernet.decrypt(enc_key_bytes)

                peers_sender_keys[sender_name] = Fernet(peer_sender_key)
                print(f"\r[{MY_NAME}] ✅ Получен и расшифрован Sender Key от {sender_name}\n[{MY_NAME}] > ", end="",
                      flush=True)

            # 2. Ищем НОВЫХ пиров и отправляем им свой Sender Key
            peers = requests.get(f"{BASE_URL}/get_peers?username={MY_NAME}").json()
            for peer_name, peer_pub_b64 in peers.items():
                if peer_name not in known_peers:
                    # Нашли новичка! Отправляем ему свой ключ
                    peer_pub_bytes = base64.b64decode(peer_pub_b64)
                    peer_pub_key = x25519.X25519PublicKey.from_public_bytes(peer_pub_bytes)

                    eph_priv = x25519.X25519PrivateKey.generate()
                    eph_pub = eph_priv.public_key()
                    shared_secret = eph_priv.exchange(peer_pub_key)
                    hkdf = HKDFExpand(algorithm=hashes.SHA256(), length=32, info=b"group-setup")
                    wrap_key = base64.urlsafe_b64encode(hkdf.derive(shared_secret))

                    temp_fernet = Fernet(wrap_key)
                    encrypted_my_key = temp_fernet.encrypt(my_sender_key)

                    requests.post(f"{BASE_URL}/send_my_sender_key", json={
                        "to_user": peer_name,
                        "from_user": MY_NAME,
                        "eph_pub": base64.b64encode(eph_pub.public_bytes(
                            serialization.Encoding.Raw, serialization.PublicFormat.Raw
                        )).decode(),
                        "enc_key": base64.b64encode(encrypted_my_key).decode()
                    })
                    known_peers.add(peer_name)
                    print(f"\r[{MY_NAME}] 📤 Отправил свой Sender Key новому пиру {peer_name}\n[{MY_NAME}] > ", end="",
                          flush=True)

        except Exception as e:
            pass  # Игнорируем ошибки сети
        time.sleep(2)  # Проверяем каждые 2 секунды


threading.Thread(target=key_exchange_loop, daemon=True).start()


# ==========================================
# ФОНОВЫЙ ПРОЦЕСС 2: ПОЛУЧЕНИЕ СООБЩЕНИЙ
# ==========================================
def listen_messages_loop():
    global known_messages_count
    print(f"\n[{MY_NAME}] Начинаю слушать сообщения. Напиши что-нибудь и нажми Enter!\n")
    while True:
        try:
            msgs = requests.get(f"{BASE_URL}/get_messages").json()
            for msg in msgs[known_messages_count:]:
                sender = msg['sender']
                payload_b64 = msg['payload']

                if sender == MY_NAME:
                    known_messages_count += 1
                    continue

                sender_fernet = peers_sender_keys.get(sender)
                if sender_fernet:
                    decrypted_text = sender_fernet.decrypt(base64.b64decode(payload_b64)).decode()
                    print(f"\r📩 Получено от {sender}: {decrypted_text}\n[{MY_NAME}] > ", end="", flush=True)
                else:
                    print(f"\r⏳ Получено сообщение от {sender}, но ключ еще не обменян. Жду...\n[{MY_NAME}] > ", end="",
                          flush=True)
                known_messages_count += 1
        except Exception:
            pass
        time.sleep(1)


threading.Thread(target=listen_messages_loop, daemon=True).start()

# ==========================================
# ГЛАВНЫЙ ПРОЦЕСС: ОТПРАВКА СООБЩЕНИЙ
# ==========================================
try:
    while True:
        text = input(f"[{MY_NAME}] > ")
        if text.strip():
            encrypted_payload = my_fernet.encrypt(text.encode())
            requests.post(f"{BASE_URL}/send_message", json={
                "from_user": MY_NAME,
                "payload": base64.b64encode(encrypted_payload).decode()
            })
except KeyboardInterrupt:
    print(f"\n[{MY_NAME}] Выход...")