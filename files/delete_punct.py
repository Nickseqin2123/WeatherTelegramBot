from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from keyboards import weather_and_delete_buttons, register_start_buttons
from sql_requests import database


router = Router(name=__name__)


class Delete(StatesGroup):
    punct = State()


@router.message(F.text == "Удалить населенный пункт")
async def delete(message: Message, state: FSMContext) -> None:
    users = [i["city"] for i in database.get_users() if i["id"] == message.from_user.id]
    if len(users) != 0:
        await state.set_state(Delete.punct)
        await message.answer(
        text="Выберите населенный пункт который хотите удалить",
        reply_markup=weather_and_delete_buttons(
            users=users)
        )


@router.message(F.text == "Главное меню")
async def cancel_handler(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return
    
    await state.clear()
    await message.answer(
        text="Мы в меню",
        reply_markup=register_start_buttons()
    )


@router.message(Delete.punct)
async def process_punct(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    data = await state.get_data()
    await state.clear()
    await summary(message=message, data=data, state=state)


async def summary(message: Message, data: dict, state: FSMContext) -> None:
    users = [i["city"] for i in database.get_users() if i["id"] == message.from_user.id]
    name = data["name"]
    if name in users:
        database.delete_punct(
            idd=message.from_user.id,
            city=name)
        await message.answer(
            text="Удаление прошло успешно!",
            reply_markup=register_start_buttons(message.from_user.id)
        )
        
    else:
        await state.set_state(Delete.punct)
        
        await message.answer(
            text="""Данного населенного пункта нет в вашем списке.
Введите населенный пункт из вашего списка"""
        )