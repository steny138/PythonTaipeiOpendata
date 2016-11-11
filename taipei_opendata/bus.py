# -*- coding: utf-8 -*-
from taipei_opendata.request import torequest
import json

class Bus(object):
        
    def route(self):
        try:
            return self.getDataDict("http://data.taipei/bus/ROUTE")
        except Exception as e:
            print e

    def stop(self, id = 0):
        try:
            dict_estimateTime = self.getDataDict("http://data.taipei/bus/Stop")

            if id > 0:
                dict_estimateTime["BusInfo"] = [item for item in dict_estimateTime["BusInfo"] if item["RouteID"] == id]

            return dict_estimateTime

        except Exception as e:
            print e

    def estimateTime(self, id = 0):
        try:
            dict_estimateTime = self.getDataDict("http://data.taipei/bus/EstimateTime")

            if id > 0:
                dict_estimateTime["BusInfo"] = [item for item in dict_estimateTime["BusInfo"] if item["RouteID"] == id]

            return dict_estimateTime

        except Exception as e:
            print e

    def getDataDict(self, url):
        data = torequest.send_request(url, compress=True)
        dataDict = json.loads(data)
        return dataDict

    """docstring for opendata"""
    def __init__(self):
        super(Bus, self).__init__()
        





