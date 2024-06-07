#Task.py
from Connection.Db_connect import db
from sqlalchemy.orm import relationship



class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    program = db.Column(db.VARCHAR(), nullable=False)
    status = db.Column(db.String(20), default='pending')
    execution_time = db.Column(db.Integer, nullable=False, default=0)
    remaining_execution_time = db.Column(db.Integer, nullable=False, default=0)
    assigned_node_id = db.Column(db.Integer, db.ForeignKey('nodes.id'))

    task_assignments = db.relationship('TaskAssignment', back_populates='task')