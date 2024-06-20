from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def start_kb(bot: str):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='➕ Добавить в чат',
                                     url=f'https://t.me/{bot}?startgroup&admin=restrict_members+delete_messages')
            ]
        ]
    )
    return markup
