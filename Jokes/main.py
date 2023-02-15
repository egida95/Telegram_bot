from telebot import types 

def button(titles: str) -> object:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
    markup.row(*titles, '|||')
    return markup


def menu():
    return button(['Шутки про программистов','Черный юмор','Туалетный юмор'])
