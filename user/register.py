from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove

from keyboards.comms import location, start_keyb
from requestss.dbreq import add_user
from requestss.other import get_locality_name


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
    lati = location.latitude
    long = location.longitude
    
    name: dict = await get_locality_name(lat=lati, lon=long)
    
    if name['type']:
        txt = await add_user(user_id=message.from_user.id, name=name['data'], lat=location.latitude, lon=location.longitude)
        await message.answer(
            text=txt, 
            reply_markup=await start_keyb()
        )
        return
    
    await message.answer(
        text=name['data'],
        reply_markup=await start_keyb()
    )