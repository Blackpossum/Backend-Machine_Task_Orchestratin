from Connection.Db_connect import db
from models.tasks import Task
from models.worker import WorkerNode
from datetime import datetime



class TaskAssignment(db.Model):
    __tablename__ = 'tasks_assignment'
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))
    node_id = db.Column(db.Integer, db.ForeignKey('worker_nodes.id'))
    assignment_time = db.Column(db.TIMESTAMP,default=datetime.now)
    completion_time = db.Column(db.TIMESTAMP)
    status = db.Column(db.String(20), default='pending')

    node = db.relationship('WorkerNode', back_populates='tasks_assignment')
    task = db.relationship('Task', back_populates='task_assignments')
    
    