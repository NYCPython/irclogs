from datetime import datetime

from .core import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    nick = db.Column(db.String(16), nullable=False) # max length of 16 comes from freenode's motd
    body = db.Column(db.Text, nullable=False)
