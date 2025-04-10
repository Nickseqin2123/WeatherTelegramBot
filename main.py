import asyncio
import logging
import configparser

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import CommandStart
from keyboards.comms import start_keyb
from main_router import router as main_router

from requests_srv.content import Content

dp = Dispatcher()
dp.include_router(
    main_router
)


@dp.message(CommandStart())
async def echo(message: Message):
    await message.answer(
        text=f'Приветствую тебя в боте в котором ты сможешь узнать погоду из любой точки мира. Нажми кнопку "Узнать погоду", чтобы продолжить.',
        reply_markup=await start_keyb()
    )


async def main():
    logging.basicConfig(level=logging.INFO)
    cnf = configparser.ConfigParser()
    cnf.read('data.ini')
    Content()
    
    bot = Bot(token=cnf['TOKEN']['token'])
    
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())