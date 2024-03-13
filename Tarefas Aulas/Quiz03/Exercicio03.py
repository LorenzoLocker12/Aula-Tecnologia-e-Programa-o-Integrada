from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = 'tasks.json'

def read_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def write_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/tasks', methods=['POST'])
def add_task():
    task_data = request.json
    data = read_data()
    task_id = str(max(map(int, data.keys())) + 1 if data else 1)
    task_data.update({'completed': False})
    data[task_id] = task_data
    write_data(data)
    return jsonify({'id': task_id}), 201

@app.route('/tasks', methods=['GET'])
def list_tasks():
    data = read_data()
    return jsonify(data)

@app.route('/tasks/<id>', methods=['PUT'])
def complete_task(id):
    data = read_data()
    if id not in data:
        return jsonify({'message': 'Task not found'}), 404
    data[id]['completed'] = True
    write_data(data)
    return jsonify({'message': 'Task completed successfully'})

@app.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    data = read_data()
    if id in data:
        del data[id]
        write_data(data)
        return jsonify({'message': 'Task deleted successfully'})
    return jsonify({'message': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
