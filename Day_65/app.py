from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

tasks = []  # In-memory storage

class Task(Resource):
    def get(self, task_id):
        task = next((task for task in tasks if task['id'] == task_id), None)
        if task:
            return jsonify(task)
        return {'message': 'Task not found'}, 404

    def put(self, task_id):
        data = request.get_json()
        for task in tasks:
            if task['id'] == task_id:
                task.update(data)
                return jsonify(task)
        return {'message': 'Task not found'}, 404

    def delete(self, task_id):
        global tasks
        tasks = [task for task in tasks if task['id'] != task_id]
        return {'message': 'Task deleted'}, 200

class TaskList(Resource):
    def get(self):
        return jsonify(tasks)

    def post(self):
        data = request.get_json()
        new_task = {
            'id': len(tasks) + 1,
            'title': data.get('title', 'Untitled Task'),
            'completed': data.get('completed', False)
        }
        tasks.append(new_task)
        return jsonify(new_task)

api.add_resource(TaskList, '/tasks')
api.add_resource(Task, '/tasks/<int:task_id>')

if __name__ == '__main__':
    app.run(debug=True)
