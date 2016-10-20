# -*- coding: utf-8 -*-

from app import db

# Create our database model
# 停車場資訊
class Park(db.Model):
    __tablename__ = "parks"

    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(100), unique=False)
    name = db.Column(db.String(100), unique=False)
    type = db.Column(db.String(2), unique=False)
    type2 = db.Column(db.String(2), unique=False)
    summary = db.Column(db.String(200), unique=False)
    address = db.Column(db.String(200), unique=False)
    tel = db.Column(db.String(50), unique=False)
    payex = db.Column(db.String(200), unique=False)
    servicetime = db.Column(db.String(50), unique=False)
    tw97x = db.Column(db.String(50), unique=False)
    tw97y = db.Column(db.String(50), unique=False)
    totalcar = db.Column(db.Integer, unique=False)
    totalmotor = db.Column(db.Integer, unique=False)
    totalbike = db.Column(db.Integer, unique=False)

    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return '<id {}>'.format(self.id)

# 剩餘車位
class ParkSeats(db.Model):
    __tablename__ = "parkSeats"

    id = db.Column(db.Integer, primary_key=True)
    availablecar =  db.Column(db.Integer, unique=False)
    availablemotor =  db.Column(db.Integer, unique=False)
   
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return '<id {}>'.format(self.id)