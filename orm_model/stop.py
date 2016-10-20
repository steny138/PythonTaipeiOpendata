# -*- coding: utf-8 -*-

from app import db

# Create our database model
class Stop(db.Model):
    __tablename__ = "stops"

    id = db.Column(db.Integer, primary_key=True)
    routeId = db.Column(db.Integer, unique=False)
    routeName =  db.Column(db.String(200), unique=False)
    seqNo =  db.Column(db.Integer, unique=False)
    longitude =  db.Column(db.String(50), unique=False)
    latitude=  db.Column(db.String(50), unique=False)
    goBack  =  db.Column(db.String(2), unique=False)

    address =  db.Column(db.String(200), unique=False)
    stopLocationId =  db.Column(db.Integer, unique=False)
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return '<id {}>'.format(self.id)