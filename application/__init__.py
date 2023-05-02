from flask import Flask
#from config import Config
import mysql.connector as mysql
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:Sole#1981@localhost/Brewry'
app.config['SECRET_KEY'] = '\x8d-\x83\x1bD\xa6\xb7wt\xa3\xc3\xef\xbd\xd8\x90\xb5\x8cJ\xba\x04\xd7,\xf8S'

db = SQLAlchemy(app)

from application import routes

