# -*- coding: utf-8 -*-

import urllib3
import gzip
import json
import StringIO
import telegram

from taipei_opendata.bus import Bus
from taipei_opendata.youbike import Youbike

class TpeBusBot(object):
    
    def handle_message(self, message):
        
        cmd, text = self.parse_cmd_text(message.text)

        self.message =message
        self.cmd = cmd
        self.text = text

        try:
            result = self.getCmd(cmd, text)  
        except Exception as e:
            print e
            return False
        return True

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
            print oriText
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
    def __init__(self, bot):
        

        super(TpeBusBot, self).__init__()
        self._bot = bot
        