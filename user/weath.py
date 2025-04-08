from aiogram import Router, F
from aiogram.types import Message


router = Router(name=__name__)


@router.message(F.text == 'Узнать погоду')
async def find_out_the_weather(message: Message):
    await message.answer(
        text='Иди зайди в Яндекс.Погода дурак.'
    )