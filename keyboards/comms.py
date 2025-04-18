from aiogram.utils.keyboard import ReplyKeyboardBuilder


async def start_keyb():
    DATA = ('Узнать погоду', 'Регистрация пункта', 'Тех.поддержка')
    builder = ReplyKeyboardBuilder()
    
    for name in DATA:
        builder.button(
            text=name
        )
    
    return builder.as_markup(resize_keyboard=True)