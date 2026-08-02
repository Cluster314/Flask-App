from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 2. Enable CORS for all routes

# Sample in-memory "database"
tasks = [
    {"id": 1, "title": "Buy groceries", "done": False},
    {"id": 2, "title": "Learn Flask", "done": True}
]

# Home route to check if the server is running
@app.route('/')
def home():
    return render_template('index.html')

# GET Request: Fetch all tasks
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks}), 200

# POST Request: Create a new task
@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({"error": "Title is required"}), 400

    new_task = {
        "id": len(tasks) + 1,
        "title": data['title'],
        "done": False
    }
    tasks.append(new_task)
    
    return jsonify(new_task), 201

if __name__ == '__main__':
    app.run(debug=True)