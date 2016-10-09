# -*- coding: utf-8 -*-


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

        # json_keyboard = json.dumps({'keyboard': [["A button"], ["B button"]], 
        #                     'one_time_keyboard': False, 
        #                     'resize_keyboard': True})


    def getCmd(self, cmd, text):
        if cmd is None or len(cmd) == 0:
            text = u'您剛剛輸入的指令是：' + text
            self._bot.sendMessage(chat_id=self.message.chat.id, text=text)
            return

        if text is None or len(text) == 0:
            return
        
        if 'lovely' in cmd:
            pass
        elif 'q' in cmd:
            pass
        elif 'set' in cmd:
            pass
        elif 'map' in cmd:
            pass
        elif 'btn' in cmd:
            pass
        elif 'lovely' in cmd:
            pass
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
        