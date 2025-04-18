from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from requests_srv.content import Content
from uti.colectiona import colect
from uti.paginator import paginate
from uti.maketxt import txt_get
from keyboards.inlines import bui


router = Router(name=__name__)


class Form(StatesGroup):
    country = State()
    region = State()
    rayon = State()
    punct = State()


@router.message(F.text == 'Регистрация пункта')
async def rtgister(message: Message, state: FSMContext):
    await state.set_state(Form.country)
    
    await message.answer(
        text='''
Давайте проведём быструю регистрацию вашего местоположения.
Введите название вашей страны.
Вы можете нажать на любую страну для копирования или же просто написать ее самому.
        '''
    )
    content: Content = Content()
    contr = await content.countries()
    
    colection = await colect(contr)
    to_pages = await paginate(colection, 13)
    await state.update_data(pages=to_pages, now=1)
    
    to_txt = await txt_get(to_pages[1])
    
    await message.answer(
        text=to_txt,
        parse_mode='MARKDOWN',
        reply_markup=await bui(now=1)
    )