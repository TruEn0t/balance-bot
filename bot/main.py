import telebot
import json
from work import *
import datetime
import os


config = json.load(open('config.json'))

bot = telebot.TeleBot(config['token'])

@bot.message_handler(content_types=['text'])
def new_message(message):

    data = find_data(message.text)
    xlsx_path = str(message.chat.id) + '.xlsx'
    date = datetime.date.today()

    #bot.send_message(message.chat.id, data.__str__())
    if data != None:

        if not os.path.isfile(xlsx_path):
            wb = openpyxl.Workbook()
            ws = wb[wb.sheetnames[0]]
            ws['a1'].value = 'Дата'
            ws['b1'].value = 'Название'
            ws['c1'].value = '-'
            ws['d1'].value = '+'
            wb.save(xlsx_path)

        wb = openpyxl.load_workbook(xlsx_path)
        ws = wb[wb.sheetnames[0]]

        ws.cell(ws.max_row + 1, 1).value = '{0}.{1}.{2}'.format(date.day, date.month, date.year)
        ws.cell(ws.max_row, 2).value = data[0]
        if data[1] < 0:
            ws.cell(ws.max_row, 3).value = abs(data[1])
        elif data[1] > 0:
            ws.cell(ws.max_row, 4).value = abs(data[1])

        wb.save(xlsx_path)

        bot.send_message(message.chat.id, 'OK')

    elif message.text.lower() in config['triggers']:
        f = open(xlsx_path, "rb")
        p = open(create_photo(xlsx_path), 'rb')
        bot.send_document(message.chat.id, f)
        bot.send_photo(message.chat.id, p)

        os.system('rm temp.png')


bot.polling(none_stop=True, interval=0)