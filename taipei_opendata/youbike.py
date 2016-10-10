# -*- coding: utf-8 -*-
from taipei_opendata.request import torequest
import json

class Youbike(object):

    def stops(self):
        try:
            url = "http://data.taipei/youbike"
            data = torequest.send_request(url, compress=False)
            bikeDict = json.loads(data)        
            return data #  bikeDict['retVal']
        except Exception as e:
            raise e
        
    """docstring for opendata"""
    def __init__(self):
        super(Youbike, self).__init__()
        





