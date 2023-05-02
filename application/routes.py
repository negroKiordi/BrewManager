from application import app, db
from flask import render_template, request, json, Response, redirect, flash, url_for, session
from application.models import OrderStatus, User
from application.forms import LoginForm


@app.route("/")
def show_tables():
	return render_template("index.html", tables = OrderStatus.query.all())

@app.route("/login", methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if request.form.get("email") == "user1@gmail.com":
			flash("You are sccessfully logged in!!!", "success")
		else:
			flash("Something went wrong.", "danger")

	return render_template("login.html", title="Loging" , form=form, login=True)

	
