from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

class User(Base):
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200))  # incase password hash becomes too long

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Pin(Base):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(140))
    image_url = db.Column(db.String(140))
    pin_by = db.relationship('User', backref=db.backref('pins', lazy='dynamic'))

    def __repr__(self):
        return '<Pin {}>'.format(self.title)


class Vote(Base):
    pin_id = db.Column(db.Integer, db.ForeignKey('pin.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    pins = db.relationship('Pin', foreign_keys=[pin_id],
                             backref=db.backref('voted_on_by', lazy='dynamic'))
    users = db.relationship('User', foreign_keys=[user_id],
                            backref=db.backref('voted_on', lazy='dynamic'))