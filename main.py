# -*- coding: utf-8 -*-
import urllib3
import gzip
import json

def main():
    # configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    urllib3.disable_warnings()
    url = "http://data.taipei/youbike"
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    
    data = r.data
    
    r.release_conn()
    bikeDict = json.loads(data)
    print data# bikeDict['retVal']
    
if __name__ == "__main__":
    main()
