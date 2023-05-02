"""
Database models
"""

from flask import Flask
from application import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy


class OrderStatus(db.Model):
	__tablename__ = 'orderstatus'

	Status = db.Column(db.String(length = 15), primary_key = True)


class User(db.Model):
    __tablename__ = 'User'
    
    email       =   db.Column(db.String(length = 40), primary_key = True)
    password    =   db.Column(db.String(length = 40))
    username    =   db.Column(db.String(length = 20))
    

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password, password)    
