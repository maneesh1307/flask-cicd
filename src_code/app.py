from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory data store
users = {}

# Helper function to validate user input
def validate_user(data):
    required_fields = ['name', 'email']
    for field in required_fields:
        if field not in data:
            return False, f"{field} is required"
    return True, None

# CREATE
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    is_valid, error = validate_user(data)
    if not is_valid:
        return jsonify({'status': False, 'message': error}), 400

    user_id = str(uuid.uuid4())
    users[user_id] = {
        'id': user_id,
        'name': data['name'],
        'email': data['email']
    }
    return jsonify({'status': True, 'data': users[user_id]}), 201

# READ ALL
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'status': True, 'data': list(users.values())}), 200

# READ ONE
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({'status': False, 'message': 'User not found'}), 404
    return jsonify({'status': True, 'data': user}), 200

# UPDATE
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({'status': False, 'message': 'User not found'}), 404

    data = request.get_json()
    user['name'] = data.get('name', user['name'])
    user['email'] = data.get('email', user['email'])
    return jsonify({'status': True, 'data': user}), 200

# DELETE
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({'status': False, 'message': 'User not found'}), 404
    del users[user_id]
    return jsonify({'status': True, 'message': 'User deleted'}), 200

# Health Check
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': True, 'message': 'API is running'}), 200

if __name__ == '__main__':
    app.run(debug=True,port=5001)
