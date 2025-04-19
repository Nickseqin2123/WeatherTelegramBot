from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove

from keyboards.comms import location, start_keyb


router = Router(name=__name__)


class Form(StatesGroup):
    cordinates = State()


@router.message(F.text == 'Регистрация пункта')
async def rtgister(message: Message, state: FSMContext):
    await state.set_state(Form.cordinates)
    
    await message.answer(
        text='''
Давайте проведём быструю регистрацию вашего местоположения.

Отправьте геолокацию по кнопке или через нажатие на Скрепку -> Геопозиция.

Предватительно отключите VPN. Это нужно для более лучшего резултата.
        ''',
        reply_markup=await location()
    )


@router.message(F.location)
async def get_loc(message: Message, state: FSMContext):
    await state.update_data(location=message.location)
    data = await state.get_data()
    await state.clear()
    
    await message.answer(text='Спасибо! Геолокация получена.', reply_markup=ReplyKeyboardRemove())
    
    await summary(message, state, data)


@router.message(F.text == 'Главное меню')
async def main_menu(message: Message, state: FSMContext):
    stat = await state.get_state()
    
    if stat is None:
        return

    await state.clear()
    await message.answer(
        text='Мы в главном меню',
        reply_markup=await start_keyb()
    )


async def summary(message: Message, state: FSMContext, data: dict):
    location = data['location']
    
    await message.answer(
        text=f'''
Широта: {location.latitude}
Долгота: {location.longitude}''',
reply_markup=await start_keyb()
    )