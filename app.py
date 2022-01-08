import telebot
import xlsConnect
from os import environ

TOKEN = environ.get('TELEBOT_TOKEN_DBDRIVE')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    cid = message.chat.id
    bot.send_message(cid, "Thanks for connecting to this bot! Type number to access blog list")

@bot.message_handler(regexp="^[-+]?[0-9]+$")
def handle_message(message):
    cid = message.chat.id

    data = xlsConnect.main(message.text)
    for _ in range(len(data)):
        bot.send_message(cid, "TITLE:"+data[_]["title"])
        bot.send_message(cid, "Date:"+data[_]["date-created"])
        print("https://darkun7.github.io/Portofolio/blog.html?article="+str(_))
