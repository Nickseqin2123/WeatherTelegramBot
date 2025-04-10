from aiogram import Router, F
from aiogram.types import Message

from requests_srv.content import countries
from uti.totxt import text_pls


router = Router(name=__name__)


@router.message(F.text == 'Узнать погоду')
async def find_out_the_weather(message: Message):
    countries_dt: list = await countries()
    to_text = text_pls(countries_dt)
    
    
    await message.answer(
        text='Мяу'
    )