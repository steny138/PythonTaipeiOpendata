# -*- coding: utf-8 -*-

from app import db

# Create our database model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    chatid =  db.Column(db.Integer, unique=False)
    last_name = db.Column(db.String(120), unique=False)
    first_name = db.Column(db.String(120), unique=False)

    # 座標
    lat = db.Column(db.String(50), unique=False)
    lng = db.Column(db.String(50), unique=False)

    # 指令
    cmd = db.Column(db.String(1000), unique=False)

    # 公車路線
    bus_route = db.Column(db.String(50), unique=False)

    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return '<id {}>'.format(self.id)