import telebot
from telebot import types
from cg import Token

bot = telebot.TeleBot(Token)

name = ''
surname = ''
age = 0 
@bot.message_handler(commands=['start'])
def Dating(message):
    bot.send_message(message.chat.id, 'Здравствуйте пользователь!')
    with open('/home/egida/lesson/bots/yourself/foto', 'rb') as stick:
        bot.send_sticker(message.chat.id, stick)
        bot.send_message(message.chat.id, 'Напишите /reg')
        
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, 'Как вас зовут?')
        with open('/home/egida/lesson/bots/yourself/foto2', 'rb') as stick:
            bot.send_sticker(message.chat.id, stick)
            bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')
        
def get_name(message):
    global name 
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у вас фамилия?')
    bot.register_next_step_handler(message, get_surname)
    
def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько вам лет?')
    bot.register_next_step_handler(message, get_age) 
    
def get_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Пишите цифрами пожалуйста')       
    bot.send_message(message.from_user.id, f'Тебе {age} лет,тебя зовут {name} {surname}?')
    bot.send_message(message.from_user.id, 'Запомню:)')
    with open('/home/egida/lesson/bots/yourself/foto3', 'rb') as stick:
        bot.send_sticker(message.chat.id, stick)

bot.polling(non_stop=True)