# -*- coding: utf-8 -*-

from taipei_opendata.bus import Bus
from taipei_opendata.youbike import Youbike

def busroute():
    try:
        to = Bus()
        print to.route()
    except Exception as e:
        print 123
        print e

if __name__ == "__main__":
    busroute();