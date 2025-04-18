from aiogram import Router, F
from aiogram.types import Message


router = Router(name=__name__)


@router.message(F.text == 'Узнать погоду')
async def weath_find(message: Message):
    await message.answer(
        text='Зайди в яндекс погоду'
    )