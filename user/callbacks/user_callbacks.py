import json
import time

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards.comms import start_keyb
from keyboards.inlines import build_paginated_keyboard
from uti.cleaner import users_last_clik
from requestss.content import Content
from uti.parsing import parser


router = Router(name=__name__)


@router.callback_query(F.func(lambda x: json.loads(x.data).get('type') == 'punct'))
async def punct_gt(callback: CallbackQuery):
    from_pars: dict = json.loads(callback.data)
    user_id = callback.from_user.id
    lati = from_pars['lat']
    long = from_pars['lon']
    
    if users_last_clik.get(user_id):
        await callback.message.answer(
            text='Ограничение по запросам 15 секунд!'
        )
        return

    users_last_clik[callback.from_user.id] = time.time()
    
    await callback.message.answer(
        text='Идёт запрос погоды...'
    )
    content = Content()
    response = await content.weather(lat=lati, lon=long)
    text = await parser(response)
    
    await callback.message.answer(
        text=text,
        reply_markup=await start_keyb()
    )


@router.callback_query(F.func(lambda x: json.loads(x.data).get('page') != 'noop' and json.loads(x.data).get('type') == 'page'))
async def page_change(callback: CallbackQuery, state: FSMContext):
    from_pars: dict = json.loads(callback.data)
    data = await state.get_data()
    pages = data['pages']
    
    await callback.message.answer(
        text='Вот ваши пункты:',
        reply_markup=await build_paginated_keyboard(pages=pages, current_page=from_pars['page'])
    )