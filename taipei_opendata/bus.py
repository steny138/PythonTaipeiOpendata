# -*- coding: utf-8 -*-
from taipei_opendata.request import torequest
import json

class Bus(object):
        
    def route(self):
        try:
            url = "http://data.taipei/bus/ROUTE"
            data = torequest.send_request(url, compress=True)
            routeDict = json.loads(data)        
            return data
        except Exception as e:
            print e

    """docstring for opendata"""
    def __init__(self):
        super(Bus, self).__init__()
        





