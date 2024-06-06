#worker.py
from Connection.Db_connect import db

class WorkerNode(db.Model):
    __tablename__ = 'worker_nodes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ip_address = db.Column(db.String(50))
    status = db.Column(db.String(20), default='active')
    workload = db.Column(db.Integer, default=0)


    # tasks = db.relationship('TasksAssignment', back_populates='node')
