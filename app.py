from flask import Flask
from Logging_config import setup_logging
from Routes.tasks import tasks_bp
from Routes.distribute_task import task_distribution_bp
from Routes.worker_nodes import worker_bp
from Routes.cnc_crud import cncCrud_bp
from Error_Handler import error_bp 
from Routes.tasks_monitoring import task_monitoring_bp
from Connection.Db_connect import db
from dotenv import load_dotenv
import os

load_dotenv()

Server_uri =os.getenv('SERVER_URI')

app = Flask(__name__)
logger = setup_logging()

app.register_blueprint(error_bp , url_prefix='/error')
app.register_blueprint(tasks_bp, url_prefix='/sig/tasks')
app.register_blueprint(task_distribution_bp, url_prefix='/sig')
app.register_blueprint(worker_bp, url_prefix='/sig/worker-nodes')
app.register_blueprint(cncCrud_bp, url_prefix='/cnc-job')
app.register_blueprint(task_monitoring_bp, url_prefix='/sig')

app.config['SQLALCHEMY_DATABASE_URI'] = Server_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)