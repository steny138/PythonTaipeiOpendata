# -*- coding: utf-8 -*-

import urllib3
import gzip
import json
import StringIO
import telegram

import orm_model

from taipei_opendata.bus import Bus
from taipei_opendata.youbike import Youbike

class TpeBusBot(object):
    
    def handle_message(self, message):
        
        cmd, text = self.parse_cmd_text(message.text)

        self.message =message
        self.cmd = cmd
        self.text = text
        self.user = orm_model.user.User.query.filter_by(id=message.from_user.id).first()
        self.processDb(message)

        try:
            result = self.getCmd(cmd, text)  

            # self._db.session.delete(self.user)
            # self._db.session.commit()

        except Exception as e:
            print e
            return False
        return True

    def processDb(self, message):
        if self.user is None:
            user = orm_model.user.User(id=message.from_user.id)

            user.chatid = message.chat.id
            user.last_name = message.from_user.last_name
            user.first_name = message.from_user.first_name

            # 座標
            if self.message.location:
                user.lat = message.location.latitude
                user.lng = message.location.longitude
            
            # 指令
            if self.cmd != "":
                user.cmd = self.cmd + ';';
            
            # 公車路線
            # bus_route = db.Column(db.String(50), unique=False)

            self._db.session.add(user)
            self._db.session.commit()
        else:
            # 指令
            if self.cmd != "":
                if self.user.cmd == None: 
                    self.user.cmd = ''

                self.user.cmd = ("%s%s;" % (self.user.cmd, self.cmd));

            # 座標
            if self.message.location:
                self.user.lat = message.location.latitude
                self.user.lng = message.location.longitude
            
            self._db.session.commit() 

    def getCmd(self, cmd, text):
        oriText = text
        text = u'您剛剛輸入的指令是：' + text

        if cmd is None or len(cmd) == 0:
            self._bot.sendMessage(chat_id=self.message.chat.id, text=text)
            return

        if oriText is None or len(oriText) == 0:
            return
        
        if 'lovely' in cmd:
            pass
        elif 'q' in cmd:
            if oriText == '299':
                self._bot.sendMessage(chat_id=self.message.chat.id, text='公車站點搜尋中, 請稍候')
                to = Bus()
                busid =11411
                stopid_goback0 =10152 # goback =0
                stopid_goback1 =10288 # goback =1

                dict_estimateTime = to.estimateTime(id=busid)
                dict_estimateTime = [item for item in dict_estimateTime["BusInfo"] if item["RouteID"] == busid and (item["StopID"] == stopid_goback0 or item["StopID"] == stopid_goback1)]

                text = u'299 捷運輔大站(建國一路)'
                for item in dict_estimateTime:
                    if item["StopID"] == stopid_goback1:
                        text = text + u'-去程'
                    else:
                        text = text + u'-回程'
                    second = int(item["EstimateTime"])
                    minute = second / 60
                    second = second % 60
                    text = text + (u'尚有%d分%d秒' % (minute, second))
                self._bot.sendMessage(chat_id=self.message.chat.id, text=text)
            else:
                pass
        elif 'set' in cmd:
            pass
        elif 'map' in cmd:
            pass
        elif 'btn' in cmd:
            pass
        elif 'c' in cmd:
            #clean postgresql data with this user id
            pass
        elif 'test' in cmd:
            print cmd
            json_keyboard = json.dumps({'keyboard': [["棕9","652"], ["227", "292", "299"]], 
                            'one_time_keyboard': True, 
                            'resize_keyboard': True})
            self._bot.sendMessage(chat_id=self.message.chat.id, text=text, reply_markup=json_keyboard)


        elif 'lovely' in cmd:
            pass
        elif 'lovely' in cmd:
            pass
        elif 'lovely' in cmd:
            pass

    def parse_cmd_text(self, text):
        # Telegram understands UTF-8, so encode text for unicode compatibility
        text = text.encode('utf-8')
        cmd = None
        if '/' in text:
            try:
                index = text.index(' ')
            except ValueError as e:
                return (text, None)
            cmd = text[:index]
            text = text[index + 1:]
        if cmd != None and '@' in cmd:
            cmd = cmd.replace(bot_name, '')
        return (cmd, text)

    """docstring for TpeBusBot"""
    def __init__(self, bot, db):
        

        super(TpeBusBot, self).__init__()
        self._bot = bot
        self._db = db
        