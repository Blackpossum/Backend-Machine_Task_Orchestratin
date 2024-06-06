from Connection.Db_connect import db
from models.tasks import Task
from sqlalchemy.orm import relationship
from datetime import datetime



class TaskAssignment():
    __tablename__ = 'tasks_assignment'
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))
    node_id = db.Column(db.Integer, db.ForeignKey('nodes.id'))
    assignment_time = db.Column(db.TIMESTAMP,default=datetime.now)
    completion_time = db.Column(db.TIMESTAMP)
    status = db.Column(db.String(20), default='pending')

    worker_node = relationship('WorkerNode', back_populates='task_assignments')
    task = relationship('Task', back_populates='task_assignments')
    from models.worker import WorkerNode