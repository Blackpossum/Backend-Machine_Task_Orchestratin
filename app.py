from flask import Flask
from Routes.tasks import tasks_bp
from Routes.distribute_task import task_distribution_bp
from Routes.worker_nodes import worker_bp
from Connection.Db_connect import db
from dotenv import load_dotenv
import os

load_dotenv()

Server_uri =os.getenv('SERVER_URI')

app = Flask(__name__)
app.register_blueprint(tasks_bp, url_prefix='/sig/tasks')
app.register_blueprint(task_distribution_bp, url_prefix='/sig/')
app.register_blueprint(worker_bp, url_prefix='/sig/worker-nodes')

app.config['SQLALCHEMY_DATABASE_URI'] = Server_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)