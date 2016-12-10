# -*- coding: utf-8 -*-

import urllib3
import gzip
import json
import StringIO
import telegram
import orm_model

from taipei_opendata.bus import Bus
from taipei_opendata.youbike import Youbike

DICT_NO_TEXT_IN_CMD = ["main"]

class TpeBusBot(object):
    def handle_message(self, message):
        # Analysis what the command that user type.
        cmd, text = self.parse_cmd_text(message.text)

        self.user = orm_model.user.User.query.filter_by(id=message.from_user.id).first()
        self.message =message
        self.cmd = cmd
        self.text = text
        
        self.track_user_behavior_from_database(message)

        try:
            result = self.get_command(cmd, text)  

            if result:
                self.clean_user_begaviro_with_database()
        except Exception as e:
            print e
            return False
        return True

    """
        track user is first or continuous enter command group.
        when user first in, it will insert a new user record preparing user send command next time.
    """
    def track_user_behavior_from_database(self, message):
        # user enter the first command group, 
        # and it will write down into database if there need second command.
        if self.user is None:
            user = orm_model.user.User(id=message.from_user.id)
            user.chatid = message.chat.id
            user.last_name = message.from_user.last_name
            user.first_name = message.from_user.first_name

            # 座標
            if message.location:
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
            if message.location:
                self.user.lat = message.location.latitude
                self.user.lng = message.location.longitude
            
            self._db.session.commit() 

    def get_command(self, cmd, text):
        isFinishBehavior = False

        oriText = text
        text = u'您剛剛輸入的內容是：' + text

        if cmd is None or len(cmd) == 0:
            self._bot.sendMessage(chat_id=self.message.chat.id, text=(text))
            return
        elif (oriText is None or len(oriText) == 0) and cmd not in DICT_NO_TEXT_IN_CMD:
            self._bot.sendMessage(chat_id=self.message.chat.id, text=('輸入無效指令%s, 你在瞎打什麼'%(cmd)))
            return

        if 'q' in cmd:
            if oriText == '299':
                self._bot.sendMessage(chat_id=self.message.chat.id, text='公車站點搜尋中, 請稍候')
                
                self.user.bus_route = oriText
                self._db.session.commit() 

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
                isFinishBehavior = True
            else:
                pass
        elif 'set' in cmd:
            pass
        elif 'map' in cmd:
            pass
        elif 'clear' in cmd:
            isFinishBehavior = True
        elif 'upgrade' in cmd:
            # upgrade some base information in postgre db ex: bus route、bus stops etc..
            if oriText == 'route':
                self._bot.sendMessage(chat_id=self.message.chat.id, text='公車路線資料庫更新中, 請稍候')
                busService = Bus()
                routes = busService.route()
                orm_model.route.Route.query.delete()

                for busroute in routes["BusInfo"]:
                    routx = orm_model.route.Route(**busroute)
                    routx.departure = busroute["departureZh"]
                    routx.destination = busroute["destinationZh"]
                    routx.routeName = busroute["nameZh"]
                    routx.ticketPriceDescription = busroute["ticketPriceDescriptionZh"]
                    
                    self._db.session.add(routx)

                self._db.session.commit()
                self._bot.sendMessage(chat_id=self.message.chat.id, text='公車路線資料庫更新完畢, 準備上路囉！')

            elif oriText == 'stop':
                self._bot.sendMessage(chat_id=self.message.chat.id, text='公車站牌資料庫更新中, 請稍候')
                busService = Bus()
                stops = busService.stop()
                orm_model.stop.Stop.query.delete()
                
                for busstop in stops["BusInfo"]:
                    stop = orm_model.stop.Stop(**busstop)
                    stop.routeName = busstop["nameZh"]
                    self._db.session.add(stop)

                self._db.session.commit()
                self._bot.sendMessage(chat_id=self.message.chat.id, text='公車站牌資料庫更新完畢, 準備上路囉！')

            isFinishBehavior = True

        elif 'main' in cmd:
            text = '您需要什麼幫助?'
            keyboard = self.get_keyboard_in_step(1, cmd)
            json_keyboard = json.dumps({'keyboard': keyboard,
                            'one_time_keyboard': True, 
                            'resize_keyboard': True})
            self._bot.sendMessage(chat_id=self.message.chat.id, text=text, reply_markup=json_keyboard)

        return isFinishBehavior

    def parse_cmd_text(self, text):
        # Telegram understands UTF-8, so encode text for unicode compatibility
        text = text.encode('utf-8')
        cmd = None
        if '/' in text or '#' in text:
            try:
                if ' ' in text:
                    index = text.index(' ')
                else:
                    index = len(text)
            except ValueError as e:
                return (None, text)
            cmd = text[1:index]
            if index > 1:
                text = text[index + 1:]

        if cmd != None and '@' in cmd:
            cmd = cmd.replace(bot_name, '')
        return (cmd, text)

    def clean_user_begaviro_with_database(self):
        self.user.lat       = None
        self.user.lng       = None
        self.user.cmd       = None
        self.user.bus_route = None

        self._db.session.commit()

    def get_keyboard_in_step(self, step, cmd):
        keyboard = [["#q 299"], 
                ["#upgrade route", "#upgrade stop"],
                [{"text": u"\U0001f579 location", "request_location":True}, {"text": u"\u260e\ufe0f phone number", "request_contact":True}]]
        return keyboard


    """docstring for TpeBusBot"""
    def __init__(self, bot, db):
        super(TpeBusBot, self).__init__()
        self._bot = bot
        self._db = db
        self.user = None
        