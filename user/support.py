from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboards.comms import main_menukeyb, start_keyb
from keyboards.inlines import base_inline


router = Router(name=__name__)


class SupportForm(StatesGroup):
    text = State()
    
    
@router.message(F.text == 'Тех.поддержка')
async def support(message: Message, state: FSMContext):
    await state.set_state(SupportForm.text)
    
    await message.answer(
        text='Укажите проблему, по которой вы обратились в службу поддержки. Админ постарается ответить вам как можно быстрее. Давайте развернутый вопрос.',
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


@router.message(SupportForm.text)
async def get_mesg(message: Message, state: FSMContext):
    data = message.text
    await state.clear()
    
    await summary(message, data)
    

async def summary(message: Message, data: str):
    user_id = message.from_user.id
    header = f'Обращение от пользователя с ID {user_id}\n\n'
    
    await message.bot.send_message(
        chat_id=1124518724, 
        text=header + data, 
        reply_markup=await base_inline(Ответить={'type': 'appeal', 'user_id': user_id})
    )
    
    await message.answer(
        text='Ваше обращение принято и в ближайшем времени будет рассмотрено! Если админ вам не ответил, то отправьте еще 1 обращение.',
        reply_markup=await start_keyb()
    )