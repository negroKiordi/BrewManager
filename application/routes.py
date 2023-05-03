from application import app, db
from flask import render_template, request, json, Response, redirect, flash, url_for, session
from application.models import OrderStatus, User
from application.forms import LoginForm



@app.route("/", methods = ['GET', 'POST'])
@app.route("/login", methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		log_email = request.form.get("email")
		q = User.query.filter_by(email=log_email).first()
		if q:
			if request.form.get("password") == q.password:  
				flash("Hello " + q.username + "!!! You are successfully logged in.", "success")
			else:
				flash("Invalid password", "danger")
		else:
			flash("Not a valid user", "danger")

	return render_template("login.html", title="Login" , form=form, login=True)

	
