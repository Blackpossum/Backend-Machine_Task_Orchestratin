from flask import Blueprint, request, jsonify
from models.tasks import Task
from Connection.Db_connect import db

tasks_bp = Blueprint('tasks', __name__)

# Create task
@tasks_bp.route('/create', methods=['POST'])
def create_task():
    data = request.get_json()
    name = data.get('name')
    program = data.get('program')
    if not name:
        return jsonify({'error': 'Name is required'}), 400
    task = Task(name=name, program=program)
    db.session.add(task)
    db.session.commit()
    return jsonify({'id': task.id, 'name': task.name, 'program': task.program}), 201

@tasks_bp.route('/show-tasks', methods=['GET'])
def get_tasks():
    try:
        # Get tasks from database
        tasks = Task.query.all()
        task_list = []
        for task in tasks:
            task_data = {
                'id': task.id,
                'name': task.name,
                'program': task.program,
                'status': task.status
            }
            task_list.append(task_data)
        # task_list = [{'id': task.id, 'name': task.name, 'description': task.description} for task in tasks]
        return jsonify(task_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@tasks_bp.route('/search', methods=['GET'])
def search_tasks():
    name = request.args.get('name')
    if not name:
        return jsonify({'error': 'Name parameter is required'}), 400
    tasks = Task.query.filter(Task.name.ilike(f'%{name}%')).all()
    task_list = [{'id': task.id, 'name': task.name, 'program': task.program} for task in tasks]
    return jsonify(task_list)

@tasks_bp.route('/update/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    data = request.get_json()
    name = data.get('name')
    program = data.get('program')
    status=data.get('status')
    if not name:
        return jsonify({'error': 'Name is required'}), 400
    task.name = name
    task.program =program
    task.status=status
    db.session.commit()
    return jsonify({'message': 'Task updated successfully'}), 200

@tasks_bp.route('/delete/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully'}), 200