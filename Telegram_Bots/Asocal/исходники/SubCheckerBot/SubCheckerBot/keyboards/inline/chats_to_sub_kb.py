from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.db_api import sql_commands


async def chats_to_sub_kb(chat_id: int, user_id: int):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f'{a["group_name"]}', url=f'{a["group_link"]}')
            ] for a in await sql_commands.select_group(chat_id)
        ]
    )
    markup.add(InlineKeyboardButton(text='✅ Я ПОДПИСАЛСЯ', callback_data=f'check_sub|{user_id}'))
    return markup
