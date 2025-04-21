from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


async def bui(now):
     bilder = InlineKeyboardBuilder()
 
     data = [
         {'name': '<<<', 'id': 'left'},
         {'name': str(now), 'id': 'num'},
         {'name': '>>>', 'id': 'right'},
 
     ]
 
     for i in data:
         bilder.add(
             InlineKeyboardButton(
                 text=i['name'],
                 callback_data=str(i['id'])
             )
         )
 
     return bilder.as_markup(resize_keyboard=True)