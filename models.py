from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
import uuid

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200))  # incase password hash becomes too long

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Pin(db.Model):
    __tablename__ = 'pins'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(140))
    image = db.Column(db.String(140))

    def __repr__(self):
        return '<Pin {}>'.format(self.text)
