#TODO ADD PEPPERING AND SALTING
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS
# from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
# os.getenv('GCP_PROJECT_ID')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
# pprint(dir(db))

from .routes import *
from .tables import *

db.create_all()