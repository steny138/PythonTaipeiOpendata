# -*- coding: utf-8 -*-

from app import db

# Create our database model
class Route(db.Model):
    __tablename__ = "routes"

    id = db.Column(db.Integer, primary_key=True)
    providerId = db.Column(db.Integer, unique=False)
    providerName = db.Column(db.String(120), unique=False)
    routeName =  db.Column(db.String(20), unique=False)
    pathAttributeId =  db.Column(db.Integer, unique=False)
    departure =  db.Column(db.String(20), unique=False)
    destination=  db.Column(db.String(20), unique=False)
    distance  =  db.Column(db.String(20), unique=False)

    goFirstBusTime =  db.Column(db.String(4), unique=False)
    backFirstBusTime =  db.Column(db.String(4), unique=False)
    goLastBusTime =  db.Column(db.String(4), unique=False)
    backLastBusTime =  db.Column(db.String(4), unique=False)

    holidayGoFirstBusTime =  db.Column(db.String(4), unique=False)
    holidayBackFirstBusTime =  db.Column(db.String(4), unique=False)
    holidayGoLastBusTime =  db.Column(db.String(4), unique=False)
    holidayBackLastBusTime =  db.Column(db.String(4), unique=False)

    segmentBuffer =  db.Column(db.String(200), unique=False)
    ticketPriceDescription =  db.Column(db.String(20), unique=False)

    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return '<id {}>'.format(self.id)