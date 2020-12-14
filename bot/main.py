import telebot
import json
from work import *
import datetime

config = json.load(open('config.json'))

bot = telebot.TeleBot(config['token'])

@bot.message_handler(content_types=['text'])
def new_message(message):

    data = find_data(message.text)

    if data:
        bot.send_message(message.chat.id, data.__str__())

bot.polling(none_stop=True, interval=0)