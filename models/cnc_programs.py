from Connection.Db_connect import db

class CNCPrograms (db.Model):
    __tablename__ = 'cnc_programs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(50))
    description = db.Column(db.String(50))
    content = db.Column(db.TEXT,nullable=False)
    created_at = db.Column(db.DateTime)