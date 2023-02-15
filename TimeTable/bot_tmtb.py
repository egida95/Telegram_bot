import telebot
from telebot import types 
from cf import token 

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здрастье')
    tm = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
    tm2 = types.KeyboardButton('Понедельник')
    tm3 = types.KeyboardButton('Вторник')
    tm4 = types.KeyboardButton('Среда')
    tm5 = types.KeyboardButton('Четверг')
    tm6 = types.KeyboardButton('Пятница')
    
    tm.add(tm2,tm3,tm4,tm5,tm6)
    
    bot.send_message(message.chat.id, 'Выберите кнобку', reply_markup=tm)
    
    @bot.message_handler(content_types=['text'])
    def timetable(message):
        if message.chat.type == 'private':
            if message.text == 'Понедельник':
                bot.send_message(message.chat.id, '1)Дене.Тарбия\n2)Орус.адабият\n3)Кыргыз.Тил\n4)Тарых\n5)Химия\n6)Алгебра')
            
            elif message.text == 'Вторник':
                bot.send_message(message.chat.id, '1)Орус.Тил\n2)Алгебра\n3)Физика\n4)ДПМ\n5)Дене.Тарбия\n6)ДПМ')
            
            elif message.text == 'Среда':
                bot.send_message(message.chat.id, '1)Кыргыз.Тил\n2)Тарых\n3)Геометрия\n4)Чет.Тил\n5)Кыргыз.Тил\n6)Геометрия')
                
            elif message.text == 'Четверг':
                bot.send_message(message.chat.id, '1)Орус.Тил\n2)Орус.Адабият\n3)Физика\n4)Кыргыз.Тил\n5)Биология\n6)Компонент')
                
            elif message.text == 'Пятница':
                bot.send_message(message.chat.id, '1)Тарых\n2)Физика\n3)Чет.Тил\n4)Кыргыз.Тил\n5)Химия\n6)География\n7)Класстык.Саат')
            
            else:
                bot.send_message(message.chat.id, 'ОШИБКА!\nВы возможно не правильно ввели дни')
                
bot.polling(non_stop=True)