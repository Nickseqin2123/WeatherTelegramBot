import json

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


async def build_paginated_keyboard(pages: dict[int, list[str]], current_page: int):
    builder = InlineKeyboardBuilder()
    
    total_pages = len(pages)
    left_arrow_json = json.dumps({'type': 'page', 'page': current_page - 1 if current_page > 1 else "noop"}, ensure_ascii=False)
    right_arrow_json = json.dumps({'type': 'page', 'page': current_page + 1 if total_pages >= current_page >= 1 else "noop"}, ensure_ascii=False)
    
    items = pages.get(current_page, [])

    for item in items:
        jso = json.dumps({'type': 'punct', 'lat': item.latitude, 'lon': item.longitude}, ensure_ascii=False)
        builder.button(text=item.name, callback_data=jso)

    builder.adjust(3)  # 3 кнопки в ряд :))))


    left_arrow = InlineKeyboardButton(
        text="◀️",
        callback_data=left_arrow_json
    )
    center = InlineKeyboardButton(
        text=f"{current_page}/{total_pages}",
        callback_data="center"
    )

    right_arrow = InlineKeyboardButton(
        text="▶️",
        callback_data=right_arrow_json
    )

    builder.row(left_arrow, center, right_arrow)

    return builder.as_markup()


async def base_inline(**kwargs):
    builder = InlineKeyboardBuilder()
    
    for text, data in kwargs.items():
        jso = json.dumps(data, ensure_ascii=False)
        builder.button(
            text=text, 
            callback_data=jso
        )
    
    return builder.as_markup(resize_keyboard=True)