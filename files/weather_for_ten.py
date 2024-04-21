from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards import weather_and_delete_buttons, register_start_buttons
from weather_ten import week_weath
from sql_requests import database


router = Router(name=__name__)


class WeatherTen(StatesGroup):
    name = State()


@router.message(F.text == "Прислать погоду на 10 дней")
async def weather(message: Message, state: FSMContext):
    users = [i["city"] for i in database.get_users() if i["id"] == message.from_user.id]
    if len(users) != 0:
        await state.set_state(WeatherTen.name)
        await message.answer(
            text="Введите населенный пункт",
            reply_markup=weather_and_delete_buttons(users=users)
        )


@router.message(F.text == "Главное меню")
async def main_menu(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.clear()
    await message.answer(
        text="Мы в меню",
        reply_markup=register_start_buttons(message.from_user.id)
    )


@router.message(WeatherTen.name)
async def wet(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    await state.clear()
    
    await summary(message=message, data=data, state=state)


async def summary(message: Message, data: dict, state: FSMContext):
    name = data["name"]
    if name not in ["Ввести данные",
                    "Прислать погоду",
                    "Интересный факт",
                    "Удалить населенный пункт",
                    "Прислать погоду на 10 дней"]:
        await message.answer(
            text="Пожалуйста подождите, запрос выполняется.Время запроса - ±8 секунд."
        )
        text = week_weath(name)
        if text != "ERROR":
            await message.answer(
                text=text,
                reply_markup=register_start_buttons(message.from_user.id)
            )
        elif text == "SEARCH ERROR":
            await message.answer(
                text="У бот ведутся тех.работы, просим вас подождать.",
                reply_markup=register_start_buttons(message.from_user.id)
            )
        else:
            await message.answer(
                text="""Вы ввели не корекктный населенный пункт.Сейчас он будет удален...
    Если вы считаете, что это ошибка, то напишите ему: @Yorichi993""",
                reply_markup=register_start_buttons(message.from_user.id)
            )
            database.delete_punct(message.from_user.id, name)
    else:
        await state.set_state(WeatherTen.name)
        
        await message.answer(
            text="Введен некорекктный населенный пункт. Введите корекктный населенный пункт"
        )