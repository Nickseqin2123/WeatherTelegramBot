import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram import types
from aiogram.filters.command import CommandStart
from keyboards import register_start_buttons
from main_router import router as main_rout


BOT_TOKEN = "6486317181:AAHmGi76R9oOJctK6p6uXAB8gDN7sB-vI6c"
dp = Dispatcher()
dp.include_router(main_rout)


@dp.message(CommandStart())
async def start_coro(message: types.Message):
    await message.answer(
        text="""Привет, Я бот который может прислать погоду из любой точки мира.
Пройдите небольшую регестрацию и начните пользоваться ботом прямо сейчас""",
        reply_markup=register_start_buttons(message.from_user.id))


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    asyncio.run(main())