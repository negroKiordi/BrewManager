#https://stackoverflow.com/questions/27766794/switching-from-sqlite-to-mysql-with-flask-sqlalchemy

import mysql.connector as mysql
from flask import Flask, render_template #, request, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Ale#1980Sole#1981@localhost/Brewry'
app.config['SECRET_KEY'] = '\x8d-\x83\x1bD\xa6\xb7wt\xa3\xc3\xef\xbd\xd8\x90\xb5\x8cJ\xba\x04\xd7,\xf8S'

db = SQLAlchemy(app)

class OrderStatus(db.Model):
	__tablename__ = 'orderstatus'

	Status = db.Column(db.String(length = 15), primary_key = True)


@app.route("/")
def show_tables():
	return render_template("index.html", tables = OrderStatus.query.all())

#print(OrderStatus.query.all())
app.run(debug=True, host="127.0.0.1", port=3000)
