from aiogram import Router, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from keyboards import register_buttons, register_start_buttons
from aiogram.types import Message
from sql_requests import database


router = Router(name=__name__)


class Form(StatesGroup):
    name = State()


@router.message(F.text == "Ввести данные")
async def command_start(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.name)
    await message.answer(
        "Введите населенный пункт",
        reply_markup=register_buttons(),
    )


@router.message(F.text == "Главное меню")
async def cancel_handler(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return
    
    await state.clear()
    await message.answer(
        "Мы в меню",
        reply_markup=register_start_buttons(message.from_user.id),
    )


@router.message(Form.name)
async def process_name(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    data = await state.get_data()
    await state.clear()
    await show_summary(message=message, data=data, state=state)


async def show_summary(message: Message, data: dict, state: FSMContext) -> None:
    name = data["name"]
    users = database.get_users()
    if name not in ["Прислать погоду",
                    "Интересный факт",
                    "Удалить населенный пункт"]:

        a = database.set_table(
            f"user_{len(users) + 1}",
            message.from_user.id,
            name.title())
        if a is not None:
            await message.answer(
                text="Введено не корекктное слово или этот населенный пункт уже находится в вашем списке",
                reply_markup=register_start_buttons(message.from_user.id)
            )
        else:
            await message.answer(
                text=f"Регистрация прошла успешно!",
                reply_markup=register_start_buttons(message.from_user.id)
            )
    else:
        await state.set_state(Form.name)
        
        await message.answer(
            text="Введен не корекктный населенный пункт. Введите корекктный населенный пункт"
        )