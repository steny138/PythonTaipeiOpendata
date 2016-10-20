# -*- coding: utf-8 -*-

from app import db

{
      "Id": 44794,
      "routeId": 15221,
      "nameZh": "埤頭里",
      "nameEn": "PitouVillage",
      "seqNo": 125,
      "pgp": "-1",
      "longitude": "121.412",
      "latitude": "25.15872",
      "goBack": "1",
      "address": "中山路一段179號同向",
      "stopLocationId": 3812,
      "showLon": "121.412",
      "showLat": "25.15872",
      "vector": "999"
    },

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