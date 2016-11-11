# -*- coding: utf-8 -*-

from app import db

# Create our database model
# youbike即時資訊
class YoubikeStop(db.Model):
    __tablename__ = "youbike_stops"

    id = db.Column(db.Integer, primary_key=True)
   
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def __init__(self, **entries):
        self.__dict__.update(entries)