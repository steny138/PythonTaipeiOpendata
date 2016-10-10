# -*- coding: utf-8 -*-

import urllib3
import gzip
import json
import StringIO
import telegram

from flask import Flask
from flask import render_template, request

from telegram_bot.tpebus import TpeBusBot
from taipei_opendata.bus import Bus
from taipei_opendata.youbike import Youbike

import sys
reload(sys)

sys.setdefaultencoding('utf-8')

app = Flask(__name__)

# execute command to create ssl crt and cem
# openssl req -new -x509 -nodes -newkey rsa:1024 -keyout server.key -out server.crt -days 3650
# execute command "ngrok http 5000" to get mag internet and localhost
# ========= CONFIG =========
DEBUG    = False
TOKEN    = '288756371:AAGwm08t-JlqF161zkBj_75syb56zqd16pM'
HOST     = 'c08693f4.ngrok.io' # Same host used when ngrok response
PORT     = 5000
# CERT     = 'server.crt'
# CERT_KEY = 'server.key'
# context = (CERT, CERT_KEY)
# ========= CONFIG =========

# ========= INITIAL =========

bot = telegram.Bot(token=TOKEN)

# ========= INITIAL =========

# ======= App controllers start ========
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
    to = Youbike()
    return to.stops()

    
@app.route("/bus/route")
def bus_route():
    to = Bus()
    return to.route()


# ======= app controllers end ========

# https://api.telegram.org/bot288756371:AAGwm08t-JlqF161zkBj_75syb56zqd16pM/setWebhook?url=https://ec8ba4c0.ngrok.io/288756371:AAGwm08t-JlqF161zkBj_75syb56zqd16pM
# https://api.telegram.org/bot288756371:AAGwm08t-JlqF161zkBj_75syb56zqd16pM/setWebhook?url=https://ycapi.herokuapp.com/bot/tpebus
def setWebhook():
    bot.setWebhook(webhook_url='https://%s/%s' % (HOST, TOKEN))

if __name__ == "__main__":
    # local used
    setWebhook()
    app.run(host='127.0.0.1',
            port=PORT,
            debug=DEBUG)