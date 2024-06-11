from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()


SECRET_URI = os.getenv('SERVER_URI')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SECRET_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models;