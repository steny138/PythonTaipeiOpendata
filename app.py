# -*- coding: utf-8 -*-

import urllib3
import gzip
import json
import StringIO
import telegram

from flask import Flask
from flask import render_template, request

from telegram_bot.tpebus import TpeBusBot

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

# Excuce command to create ssl crt and cem
# openssl req -new -x509 -nodes -newkey rsa:1024 -keyout server.key -out server.crt -days 3650

# execeut command "ngrok http 5000" to get mag internet and localhost
# ========= CONFIG =========
DEBUG    = False
TOKEN    = '288756371:AAGwm08t-JlqF161zkBj_75syb56zqd16pM'
HOST     = '610d2e28.ngrok.io' # Same host used when ngrok response
PORT     = 5000
# CERT     = 'server.crt'
# CERT_KEY = 'server.key'
# context = (CERT, CERT_KEY)
# ========= CONFIG =========

bot = telegram.Bot(token=TOKEN)



@app.route("/")
def hello():
    return "Hello! Welcome to yuchen's Home"

@app.route('/<token>', methods=['POST'])
def launcher(token):
    if request.method == "POST":
        try:
            handler = TpeBusBot(bot)
            
            update = telegram.Update.de_json(request.get_json(force=True), bot)
            message = update.message
            
            isSuccess = handler.handle_message(message)

            return 'ok'
        except Exception as e:
            print e
    return 'ok'

# telegram yctpebusbot
@app.route("/bot/tpebus", methods=['POST'])
def botHook_tpebus():
    try:
        handler = TpeBusBot(bot)
        
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        message = update.message
        
        isSuccess = handler.handle_message(message)

        return 'ok'
    except Exception as e:
        print e
    

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

# https://api.telegram.org/bot288756371:AAGwm08t-JlqF161zkBj_75syb56zqd16pM/setWebhook?url=https://ec8ba4c0.ngrok.io/288756371:AAGwm08t-JlqF161zkBj_75syb56zqd16pM
# https://api.telegram.org/bot288756371:AAGwm08t-JlqF161zkBj_75syb56zqd16pM/setWebhook?url=https://ycapi.herokuapp.com/bot/tpebus
def setWebhook():
    bot.setWebhook(webhook_url='https://%s/%s' % (HOST, TOKEN))

if __name__ == "__main__":
    setWebhook()
    app.run(host='127.0.0.1',
            port=PORT,
            debug=DEBUG)