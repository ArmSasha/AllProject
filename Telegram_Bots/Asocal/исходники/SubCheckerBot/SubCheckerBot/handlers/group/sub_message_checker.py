from aiogram import types
from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram.types import ChatPermissions

from keyboards import chats_to_sub_kb
from loader import dp
from utils.db_api import sql_commands


@dp.message_handler(ChatTypeFilter(chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP]))
async def check_sub_member_group(message: types.Message):
    groups = await sql_commands.select_group(message.chat.id)
    for group in groups:
        sub = await dp.bot.get_chat_member(group["group_id"], message.from_user.id)
        if sub.status == 'left':
            await message.bot.restrict_chat_member(message.chat.id,
                                                   message.from_user.id,
                                                   ChatPermissions(can_send_messages=False)
                                                   )
            await message.delete()
            await message.answer(f'*❗️ Упс, [{message.from_user.first_name}](tg://user?id={message.from_user.id}), *'
                                 f'*кажется вы не подписаны на наши чаты*',
                                 parse_mode=types.ParseMode.MARKDOWN_V2,
                                 reply_markup=await chats_to_sub_kb(message.chat.id,
                                                                    message.from_user.id
                                                                    )
                                 )
