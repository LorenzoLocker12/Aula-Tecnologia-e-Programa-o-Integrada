from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = 'users.json'

def read_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def write_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.json
    data = read_data()
    user_id = str(max(map(int, data.keys())) + 1 if data else 1)
    data[user_id] = user_data
    write_data(data)
    return jsonify({'id': user_id}), 201

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    data = read_data()
    user = data.get(id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(user)

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    user_data = request.json
    data = read_data()
    if id not in data:
        return jsonify({'message': 'User not found'}), 404
    data[id] = user_data
    write_data(data)
    return jsonify({'message': 'User updated successfully'})

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    data = read_data()
    if id in data:
        del data[id]
        write_data(data)
        return jsonify({'message': 'User deleted successfully'})
    return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
