from flask import Blueprint,request,jsonify
from Connection.Db_connect import db
from models.worker import WorkerNode

worker_bp = Blueprint('worker', __name__)

# Create a new worker node
@worker_bp.route('/create', methods=['POST'])
def create_worker_node():
    data = request.get_json()
    name = data.get('name')
    ip_address = data.get('ip_address')
    status = data.get('status')
    workload = data.get('workload')
    # You can add more fields such as IP address, status, etc. as needed
    if not name:
        return jsonify({'error': 'Name is required'}), 400
    worker_node = WorkerNode(name=name, ip_address=ip_address, status=status, workload=workload)
    db.session.add(worker_node)
    db.session.commit()
    return jsonify({'id': worker_node.id, 'name': worker_node.name, 'ip_address':worker_node.ip_address, 'status':worker_node.status, 'worload':worker_node.workload}), 201

# Retrieve all worker nodes
@worker_bp.route('/show-nodes', methods=['GET'])
def get_worker_nodes():
    worker_nodes = WorkerNode.query.all()
    worker_node_list = [{'id': node.id, 'name': node.name, 'ip_address':node.ip_address, 'status':node.status, 'worload':node.workload} for node in worker_nodes]
    return jsonify(worker_node_list)

# Retrieve a single worker node by its ID
@worker_bp.route('/<int:node_id>', methods=['GET'])
def get_worker_node(node_id):
    worker_node = WorkerNode.query.get(node_id)
    if not worker_node:
        return jsonify({'error': 'Worker node not found'}), 404
    return jsonify({'id': worker_node.id, 'name': worker_node.name})

# Update an existing worker node
@worker_bp.route('/update/<int:node_id>', methods=['PUT'])
def update_worker_node(node_id):
    worker_node = WorkerNode.query.get(node_id)
    if not worker_node:
        return jsonify({'error': 'Worker node not found'}), 404
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({'error': 'Name is required'}), 400
    worker_node.name = name
    db.session.commit()
    return jsonify({'message': 'Worker node updated successfully'}), 200

# Delete a worker node
@worker_bp.route('/delete/<int:node_id>', methods=['DELETE'])
def delete_worker_node(node_id):
    worker_node = WorkerNode.query.get(node_id)
    if not worker_node:
        return jsonify({'error': 'Worker node not found'}), 404
    db.session.delete(worker_node)
    db.session.commit()
    return jsonify({'message': 'Worker node deleted successfully'}), 200