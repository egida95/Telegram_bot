import telebot
from telebot import types
from cn import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здрая желаю вам,дорогой пользователь!', reply_markup=[])
    