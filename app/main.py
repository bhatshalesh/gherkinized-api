from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    title = data.get('title')
    if not title:
        return jsonify({"error": "Title is required"}), 400
    task = {"id": len(tasks) + 1, "title": title}
    tasks.append(task)
    return jsonify(task), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
