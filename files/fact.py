from aiogram import F
from aiogram import Router
from aiogram.types import Message
from fact_pars import get_fact


router = Router(name=__name__)


@router.message(F.text == "Интересный факт")
async def fact(message: Message):
    await message.answer(
        text=get_fact()
    )
