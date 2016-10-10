# -*- coding: utf-8 -*-

import urllib3
import gzip
import json
import StringIO
import telegram

from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy
from flask import render_template, request

from telegram_bot.tpebus import TpeBusBot
from taipei_opendata.bus import Bus
from taipei_opendata.youbike import Youbike

import sys
import os
reload(sys)

sys.setdefaultencoding('utf-8')

app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)


# execute command to create ssl crt and cem
# openssl req -new -x509 -nodes -newkey rsa:1024 -keyout server.key -out server.crt -days 3650
# execute command "ngrok http 5000" to get mag internet and localhost
# ========= CONFIG =========
DEBUG    = False
TOKEN    = '288756371:AAGwm08t-JlqF161zkBj_75syb56zqd16pM'
HOST     = '57f48e9d.ngrok.io' # Same host used when ngrok response
PORT     = 5000
# CERT     = 'server.crt'
# CERT_KEY = 'server.key'
# context = (CERT, CERT_KEY)
# add   ~/.bash_profile file next command
# export DATABASE_URL="postgresql://localhost/ycapi"
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
# postgres://pbceotosmxjyvp:-2q3aYoUC2KVBmNZ4-1z44NXq0@ec2-54-163-249-150.compute-1.amazonaws.com:5432/d8pnbion83577c

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