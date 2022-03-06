from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql

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
        return '<Pin {}>'.format(self.image_url)

    def to_json(self):
        return {
                'id': self.id,
                'title': self.title,
                'image_url': self.image_url,
                'pin_by': self.pin_by.username if self.pin_by is not None else ''
            }

class Vote(Base):
    pin_id = db.Column(db.Integer, db.ForeignKey('pin.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    pins = db.relationship('Pin', foreign_keys=[pin_id],
                             backref=db.backref('voted_on_by', lazy='dynamic'))
    users = db.relationship('User', foreign_keys=[user_id],
                            backref=db.backref('voted_on', lazy='dynamic'))

class PinDetail(Base):
    id = db.Column(db.Integer, primary_key=True)
    pin_id = db.Column(db.Integer, db.ForeignKey('pin.id'))
    caption = db.Column(db.String(140))
    tags = db.Column(postgresql.ARRAY(db.String))
    pin = db.relationship('Pin', foreign_keys=[pin_id],
                        backref=db.backref('pin_detail', lazy='dynamic', cascade="all,delete"))

    def __repr__(self):
        return '<PinDetail {}>'.format(self.pin.image_url)