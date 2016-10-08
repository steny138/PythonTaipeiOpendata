import StringIO
import urllib3
import gzip
import json

def busroute():
    try:
        urllib3.disable_warnings()
        url = "http://data.taipei/bus/ROUTE"
        
        data = send_request(url, compress=True)
        print data #  bikeDict['retVal']
    except Exception as e:
        print 123
        print e

def send_request(url, compress = False):
    urllib3.disable_warnings()
    http = urllib3.PoolManager()
    r = http.request('GET', url, preload_content=False)
    if compress:
        data = decompressGzip(r.read())
    else: 
        data = r.read()
    r.release_conn()
    return data

def decompressGzip(compressStr):
    compressedStram = StringIO.StringIO()
    compressedStram.write(compressStr)
    compressedStram.seek(0)
    decompressedStream = gzip.GzipFile(fileobj=compressedStram, mode='rb')
    result = decompressedStream.read()
    return result

if __name__ == "__main__":
    busroute();