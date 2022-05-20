import telebot
import requests
import time
from sendler import Sendler

TOKEN = '5380750605:AAHOdCKr8kvl6Tro94je8U0Vtw1QwXbqp6Y'




class TelegramBot(Sendler):
    def __init__(self, token):
        self.token = token
        self.members_id = []

    def get_updates(self, offset=0):
        result = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates?offset={offset}').json()
        self.last_update = result


    def send_message(self, data):
        
        self.bot.send_message

    def run(self):
        self.get_updates()
        self.update_id = self.last_update['result'][-1]['update_id'] # ѕрисваиваем ID последнего отправленного сообщени€ боту
        while True:
           time.sleep(2)
           self.get_updates()
           self.messages = self.last_update['result'] # ѕолучаем обновлени€
           for self.message in self.messages:
            # ≈сли в обновлении есть ID больше чем ID последнего сообщени€, значит пришло новое сообщение
               if self.update_id < self.message['update_id']:
                    self.update_id = self.message['update_id'] # ѕрисваиваем ID последнего отправленного сообщени€ боту
                    print(self.update_id)

bot = TelegramBot(token='5380750605:AAHOdCKr8kvl6Tro94je8U0Vtw1QwXbqp6Y')
bot.run()