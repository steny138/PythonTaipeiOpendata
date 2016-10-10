# -*- coding: utf-8 -*-

from taipei_opendata.bus import Bus
from taipei_opendata.youbike import Youbike

def busroute():
    try:
        busid =11411
        stopid_goback0 =10152 # goback =0
        stopid_goback1 =10288 # goback =1
        to = Bus()
        dict_estimateTime = to.estimateTime(id=busid)
        dict_estimateTime = [item for item in dict_estimateTime["BusInfo"] if item["RouteID"] == busid and (item["StopID"] == stopid_goback0 or item["StopID"] == stopid_goback1)]

        text = u'299 捷運輔大站(建國一路)'
        for item in dict_estimateTime:
            if item["StopID"] == stopid_goback1 :
                text = text + u'-去程'
            else:
                text = text + u'-回程'
            second = int(item["EstimateTime"])
            minute = second / 60
            second = second % 60
            text = text + (u'尚有%d分%d秒' % (minute, second))

        print dict_estimateTime
        print text.encode('utf-8').strip()
    except Exception as e:
        print 123
        print e

if __name__ == "__main__":
    busroute();