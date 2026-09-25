from flask import Flask, request, jsonify

app = Flask(__name__)

users_db = {}
sender_keys_mailbox = {}  # Почтовые ящики для обмена ключами
messages_db = []

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    users_db[data['username']] = data['pub_key']
    sender_keys_mailbox[data['username']] = []
    print(f"[SERVER] User {data['username']} registered.")
    return jsonify({"status": "ok"})

@app.route('/get_peers', methods=['GET'])
def get_peers():
    my_name = request.args.get('username')
    peers = {name: key for name, key in users_db.items() if name != my_name}
    return jsonify(peers)

@app.route('/send_my_sender_key', methods=['POST'])
def send_sender_key():
    data = request.json
    recipient = data['to_user']
    if recipient in sender_keys_mailbox:
        sender_keys_mailbox[recipient].append({
            "sender": data['from_user'],
            "eph_pub": data['eph_pub'],
            "enc_key": data['enc_key']
        })
    return jsonify({"status": "ok"})

# НОВЫЙ ЭНДПОИНТ: Отдает ключи и очищает ящик
@app.route('/pop_my_sender_keys', methods=['GET'])
def pop_sender_keys():
    my_name = request.args.get('username')
    keys = sender_keys_mailbox.get(my_name, [])
    sender_keys_mailbox[my_name] = [] # Очищаем, чтобы не расшифровывать дважды
    return jsonify(keys)

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    messages_db.append({
        "sender": data['from_user'],
        "payload": data['payload']
    })
    print(f"[SERVER] Message from {data['from_user']} added to group.")
    return jsonify({"status": "ok"})

@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify(messages_db)

if __name__ == '__main__':
    print("[SERVER] Starting blind relay server on port 5000...")
    app.run(port=5000, debug=False, use_reloader=False)