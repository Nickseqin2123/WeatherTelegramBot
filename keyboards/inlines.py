from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


async def build_paginated_keyboard(pages: dict[int, list[str]], current_page: int):
    builder = InlineKeyboardBuilder()

    items = pages.get(current_page, [])

    for item in items:
        builder.button(text=item.name, callback_data=f"item:{item}")

    builder.adjust(3)  # 3 кнопки в ряд :))))

    total_pages = len(pages)

    left_arrow = InlineKeyboardButton(
        text="◀️",
        callback_data=f"page:{current_page - 1}" if current_page > 1 else "noop"
    )

    center = InlineKeyboardButton(
        text=f"{current_page}/{total_pages}",
        callback_data="center"
    )

    right_arrow = InlineKeyboardButton(
        text="▶️",
        callback_data=f"page:{current_page + 1}" if current_page < total_pages else "noop"
    )

    builder.row(left_arrow, center, right_arrow)

    return builder.as_markup()