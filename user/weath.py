from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State


from requestss.dbreq import get_puncts
from keyboards.comms import start_keyb, main_menukeyb
from uti.paginator import paginator
from keyboards.inlines import build_paginated_keyboard


router = Router(name=__name__)


class Actions(StatesGroup):
    menu = State()
    

@router.message(F.text == 'Узнать погоду')
async def weath_find(message: Message, state: FSMContext):
    response: list | str = await get_puncts(user_id=message.from_user.id)

    if isinstance(response, list):
        await message.answer(
            text='Чуть-чуть подождите. Идет обработка данных...',
            reply_markup=await main_menukeyb()
        )
        
        await state.set_state(Actions.menu)
        pages = await paginator(response, 3)
        
        await state.update_data(pages=pages)
        
        await message.answer(
            text='Вот ваши пункты:',
            reply_markup=await build_paginated_keyboard(pages=pages, current_page=1)
        )
        
        return
    
    await message.answer(
        text=response
    )


@router.message(F.text == 'Главное меню')
async def main_menu(message: Message, state: FSMContext):
    stat = await state.get_state()
    
    if stat is None:
        return
    
    await state.clear()
    await message.answer(
        text='Мы в главном меню.',
        reply_markup=await start_keyb()
    )