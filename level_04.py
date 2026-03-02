from flask import Flask, request, jsonify, render_template

# Task 10: Mini To-Do REST API
"""
Goal:
    Practice CRUD fundamentals in Flask by building a simple To-Do API
    using an in-memory Python list as the data store.

What I will learn:
    1. Building RESTful API routes (GET, POST, DELETE)
    2. Handling JSON input and output
    3. Managing in-memory data structures
    4. Auto-incrementing resource IDs
    5. Returning clean, structured JSON responses

Requirements:
    1. GET /todos
        - Return all todos in JSON format.
        - Response example:
            [
                {"id": 1, "task": "Buy milk"},
                {"id": 2, "task": "Clean room"}
            ]

    2. POST /todos
        - Accept JSON input: {"task": "<task_name>"}
        - Add the todo to the list with an auto-incremented ID.
        - Return JSON:
            {"message": "Todo added", "id": <new_id>}

    3. DELETE /todos/<id>
        - Remove the todo with the given ID.
        - If successful, return:
            {"message": "Todo deleted"}
        - If ID does not exist, return:
            {"error": "Todo not found"}

Notes:
    - Use a global list for storing todos.
    - Each todo must be a dictionary: {"id": int, "task": str}
    - Ensure IDs auto-increment correctly.
    - All responses must be JSON (use jsonify()).
"""

app = Flask(__name__)

# Global List for tracking tasks

task = []
current_task_id = 1

@app.route("/")
def default_route():
    return f"This is Default Route, avaialables routes are: [GET '/todos', DELETE '/todos/<id>', POST '/todos', '']"

@app.route("/todos", methods = ["GET", "POST"])
def todos():
    global task
    global current_task_id

    if request.method == "GET":
        return jsonify(task)

    if request.method == "POST":
        data = request.get_json()
        task_name = data.get("task_name")
        task.append({"id": current_task_id, "task": task_name})
        task_id = current_task_id
        current_task_id += 1
        return jsonify({
            "message": f"'{task_name}' added to Todo List",
            "id": task_id
        })

@app.route("/todos/<int:task_id>", methods = ["DELETE"])
def delete_todo(task_id: int):
    global task
    global current_task_id

    if task_id > 0:
        if task_id > current_task_id:
            return jsonify({
                "error": f"Only {current_task_id} Todo's have been added, give task_id <= {current_task_id}"
            })
        
        else:
            for i in range(len(task)):
                if task[i]["id"] == task_id:
                    task_to_remove = task[i]["task"]
                    task.pop(i)
                    break
            return jsonify({
                "message": f"`{task_to_remove}` deleted"
            })

if __name__ == "__main__":
    app.run(debug = True)