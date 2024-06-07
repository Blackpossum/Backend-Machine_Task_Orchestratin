import time
from flask import Blueprint, jsonify
from models.tasks import Task
from models.tasks_assignment import TaskAssignment
from Connection.Db_connect import db

task_monitoring_bp = Blueprint('task_monitoring', __name__)

@task_monitoring_bp.route('/monitor-tasks', methods=['GET'])
def monitor_tasks():
    try:
        # Retrieve all task assignments
        task_assignments = TaskAssignment.query.all()
        
        # Update task status based on completion
        for task_assignment in task_assignments:
            task = Task.query.get(task_assignment.task_id)
            if task.status == 'assigned':
                # Check if the CNC code is assigned
                # Split the CNC code into individual lines
                # Execute each line of the CNC code
                if task.program:
                    cnc_lines = task.program.split('\n')
                    for line in cnc_lines:
                        # Simulate node working on CNC code
                        time.sleep(5)  #interval 5 second
                        # Execute the CNC code line (simulate execution)
                        print(f'Executing CNC code line: {line}')
        
        return jsonify({'message': 'Task monitoring completed'}), 200
    except Exception as e:
        print(e)
        return jsonify({'error': 'Failed to monitor tasks'}), 500
