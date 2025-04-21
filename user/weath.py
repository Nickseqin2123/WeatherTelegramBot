from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State


from requestss.dbreq import get_puncts
from requestss.content import Content
from keyboards.comms import start_keyb
from keyboards.inlines import puncts_butt


router = Router(name=__name__)


class Menu(StatesGroup):
    menu = State()
    

@router.message(F.text == 'Узнать погоду')
async def weath_find(message: Message, state: FSMContext):
    response: list | str = await get_puncts(user_id=message.from_user.id)
    
    if isinstance(response, list):
        
        await message.answer(
            text='Вот ваши зарегестрированные пункты.',
            reply_markup=await puncts_butt()
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