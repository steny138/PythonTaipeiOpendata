import urllib3
import gzip
import json

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/youbike")
def youbike():
	# configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    urllib3.disable_warnings()
    url = "http://data.taipei/youbike"
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    
    data = r.data
    
    r.release_conn()
    bikeDict = json.loads(data)
    return data# bikeDict['retVal']

if __name__ == "__main__":
    app.run(host='0,0,0,0', port=80)