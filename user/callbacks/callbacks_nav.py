from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from uti.maketxt import txt_get
from keyboards.inlines import bui


router = Router(name=__name__)


@router.callback_query(F.data == 'right')
async def right(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    now = data['now'] + 1
    pages: dict = data['pages']
    
    await state.update_data(now=now)
    to_txt = await txt_get(pages.get(now))
    
    await callback.message.edit_text(
        text=to_txt,
        reply_markup=await bui(now),
        parse_mode='MARKDOWN')


@router.callback_query(F.data == 'left')
async def right(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    now = data['now'] - 1
    pages = data['pages']
    
    await state.update_data(now=now)
        
    to_txt = await txt_get(pages.get(now))
        
    await callback.message.edit_text(
        text=to_txt,
        reply_markup=await bui(now),
        parse_mode='MARKDOWN'
        )