from flask import Blueprint, jsonify
from models.worker import WorkerNode
from models.tasks import Task
from Connection.Db_connect import db

task_distribution_bp = Blueprint('task_distribution', __name__)

@task_distribution_bp.route('/distribute-tasks', methods=['POST'])
def distribute_tasks():
    try:
        # Retrieve available worker nodes
        available_nodes = WorkerNode.query.filter_by(status='active').all()
        
        if not available_nodes:
            return jsonify({'error': 'No available worker nodes found'}), 400
        
        # Retrieve pending tasks
        tasks = Task.query.filter_by(status='pending').all()
        
        if not tasks:
            return jsonify({'error': 'No pending tasks found'}), 400
        
        # Initialize index for round-robin assignment
        node_index = 0
        
        # Distribute tasks evenly among available nodes
        for task in tasks:
            # Get the current node for assignment (round-robin)
            current_node = available_nodes[node_index % len(available_nodes)]
            
            # Assign the task to the current node
            task.status = 'assigned'
            task.assigned_node_id = current_node.id
            
            # Increment the index for round-robin assignment
            node_index += 1
        
        # Update the status of tasks in the database
        db.session.commit()
        
        return jsonify({'message': 'Tasks distributed successfully'}), 200
    except Exception as e:
        print(e)
        return jsonify({'error': 'Failed to distribute tasks'}), 500

