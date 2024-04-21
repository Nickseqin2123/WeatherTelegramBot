from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from sql_requests import database


def get_start_buttons():    
    buttons = ["Ввести данные", "Интересный факт"]
    
    builder = ReplyKeyboardBuilder()
    for buton in buttons:
        builder.button(text=buton)

    builder.adjust(3)
    return builder.as_markup(resize_keyboard=True)


def register_buttons():
    button = [KeyboardButton(text="Главное меню")]
    markup = ReplyKeyboardMarkup(keyboard=[button], resize_keyboard=True)
    return markup


def register_start_buttons(idd):
    users = database.get_users()
    if len([i for i in users if i["id"] == idd]) != 0:
        buttons = ["Ввести данные",
                   "Прислать погоду",
                   "Интересный факт",
                   "Удалить населенный пункт",
                   "Прислать погоду на 10 дней"]
        
        builder = ReplyKeyboardBuilder()
        
        for butt in buttons:
            builder.button(text=butt)
        
        builder.adjust(3)
        return builder.as_markup(resize_keyboard=True)
    return get_start_buttons()


def weather_and_delete_buttons(users: list):
    user_city = users + ["Главное меню"]
    
    buider = ReplyKeyboardBuilder()
    for city in user_city:
        buider.button(text=city)
    
    buider.adjust(3)
    return buider.as_markup(resize_keyboard=True)