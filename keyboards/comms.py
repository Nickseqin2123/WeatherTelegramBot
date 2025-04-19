from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


async def start_keyb():
    DATA = ('Узнать погоду', 'Регистрация пункта', 'Тех.поддержка')
    builder = ReplyKeyboardBuilder()
    
    for name in DATA:
        builder.button(
            text=name
        )
    
    return builder.as_markup(resize_keyboard=True)


async def location():
    location_keyboard = ReplyKeyboardMarkup(keyboard=[
            [
             KeyboardButton(text="Отправить геолокацию", request_location=True), 
             KeyboardButton(text="Главное меню")
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True)

    return location_keyboard