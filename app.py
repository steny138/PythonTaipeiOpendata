import urllib3
import gzip
import json
import StringIO

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!2"

@app.route("/youbike")
def youbike():
    # configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    url = "http://data.taipei/youbike"
    data = send_request(url)
    bikeDict = json.loads(data)        
    return data #  bikeDict['retVal']
    
@app.route("/bus/route")
def busroute():
    try:
        url = "http://data.taipei/bus/ROUTE"
        data = send_request(url, compress=True)
        routeDict = json.loads(data)        
        return data #  bikeDict['retVal']
    except Exception as e:
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
    app.run()