from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room
from datetime import datetime

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

users_pub_keys = {}
rooms_metadata = {}


@socketio.on('connect')
def handle_connect():
    print(f"[SERVER] 🔌 Клиент подключился. SID: {request.sid}")


@socketio.on('register_user')
def handle_register(data):
    user_id = data['user_id']
    pub_key = data['pub_key']
    users_pub_keys[user_id] = pub_key
    join_room(user_id)  # Личная комната для прямых сообщений
    print(f"[SERVER] 📝 Зарегистрирован: {user_id}")


@socketio.on('join_group')
def handle_join(data):
    group_id = data['group_id']
    user_id = data['user_id']

    join_room(group_id)

    if group_id not in rooms_metadata:
        rooms_metadata[group_id] = {'members': [], 'last_activity': datetime.now()}

    existing_members = rooms_metadata[group_id]['members'].copy()
    rooms_metadata[group_id]['members'].append(user_id)
    rooms_metadata[group_id]['last_activity'] = datetime.now()

    new_user_pub_key = users_pub_keys.get(user_id)
    print(f"[SERVER] ✅ {user_id} вошел в группу '{group_id}'")

    emit('system_message', {'text': f"{user_id} присоединился к чату"}, room=group_id)

    # Сообщаем старым участникам о новом
    for member in existing_members:
        emit('new_member_joined', {
            'new_user_id': user_id,
            'new_user_pub_key': new_user_pub_key
        }, room=member)

    # Сообщаем новому участнику о старых
    existing_members_info = {}
    for member in existing_members:
        if member in users_pub_keys:
            existing_members_info[member] = users_pub_keys[member]

    emit('existing_members_info', {
        'group_id': group_id,
        'members': existing_members_info
    }, room=user_id)


@socketio.on('leave_group')
def handle_leave(data):
    group_id = data['group_id']
    user_id = data['user_id']
    leave_room(group_id)

    if group_id in rooms_metadata:
        if user_id in rooms_metadata[group_id]['members']:
            rooms_metadata[group_id]['members'].remove(user_id)
        rooms_metadata[group_id]['last_activity'] = datetime.now()

    print(f"[SERVER] 🚪 {user_id} вышел из '{group_id}'")
    emit('system_message', {'text': f"{user_id} покинул чат"}, room=group_id)

    # КРИТИЧЕСКИ ВАЖНО: Уведомляем оставшихся, чтобы они сменили ключи шифрования!
    emit('member_left', {'group_id': group_id, 'user_id': user_id}, room=group_id)


@socketio.on('send_message')
def handle_message(data):
    group_id = data['group_id']
    sender_id = data['sender_id']
    payload = data['payload']

    if group_id in rooms_metadata:
        rooms_metadata[group_id]['last_activity'] = datetime.now()

    print(f"[SERVER] 💬 Сообщение от {sender_id} в '{group_id}'")
    emit('new_message', {
        "group_id": group_id,
        "sender_id": sender_id,
        "payload": payload
    }, room=group_id)


@socketio.on('send_my_sender_key')
def handle_send_my_sender_key(data):
    target_user = data['target_user']
    emit('receive_sender_key', data, room=target_user)


@socketio.on('disconnect')
def handle_disconnect():
    print(f"[SERVER] 🔌 Клиент отключился. SID: {request.sid}")


@app.route('/rooms')
def get_rooms_info():
    return jsonify(rooms_metadata)


if __name__ == '__main__':
    print("🚀 [SERVER] Запуск сервера на порту 5000 (режим threading)...")
    socketio.run(app, host='127.0.0.1', port=5000, debug=False)