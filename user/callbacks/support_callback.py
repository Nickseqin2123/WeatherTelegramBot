import json

from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from keyboards.comms import main_menukeyb, start_keyb


router = Router(name=__name__)


class From(StatesGroup):
    text = State()


@router.callback_query(F.func(lambda x: json.loads(x.data).get('type') == 'appeal'))
async def reply_support(callback: CallbackQuery, state: FSMContext):
    data = json.loads(callback.data)
    
    await state.update_data(id_user=data['user_id'])
    await state.set_state(From.text)
    
    await callback.message.answer(
        text='Напишите ваш ответ.',
        reply_markup=await main_menukeyb()
    )


@router.message(F.text == 'Главное меню')
async def go_menu(message: Message, state: FSMContext):
    current_state = await state.get_state()
    
    if current_state is None:
        return
    
    await state.clear()
    await message.answer(
        text='Мы в главном меню.',
        reply_markup=await start_keyb()
    )


@router.message(From.text)
async def get_mesg(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    
    data = await state.get_data()
    await state.clear()
    
    await summary(message, data)


async def summary(message: Message, data: str):
    to_user = data['id_user']
    text_to = data['text']
    header = 'Ответ от админа:\n\n'
    
    await message.bot.send_message(
        chat_id=to_user, 
        text=header + text_to
    )
    await message.answer(
        text='Сообщение отправлено!',
        reply_markup=await start_keyb()
    )