from aiogram import types
from aiogram.types import ContentType, ChatPermissions

from keyboards import chats_to_sub_kb
from loader import dp
from utils.db_api import sql_commands


@dp.message_handler(content_types=[ContentType.NEW_CHAT_MEMBERS])
async def new_chat_member(message: types.Message):
    subscribed = 0
    groups = await sql_commands.select_group(message.chat.id)
    for group in groups:
        sub = await dp.bot.get_chat_member(group["group_id"], message.from_user.id)
        if sub.status != types.ChatMemberStatus.LEFT:
            subscribed += 1
        else:
            await message.bot.restrict_chat_member(message.chat.id,
                                                   message.from_user.id,
                                                   ChatPermissions(can_send_messages=False)
                                                   )
            await message.reply(f'*👋 Привет, [{message.from_user.first_name}](tg://user?id={message.from_user.id}) *\n'
                                f'_Пожалуйста, подпишитесь на наши чаты, чтобы иметь возможность отправлять сообщения в этой группе_',
                                parse_mode=types.ParseMode.MARKDOWN_V2,
                                reply_markup=await chats_to_sub_kb(message.chat.id,
                                                                   message.from_user.id
                                                                   )
                                )
            break
    else:
        await message.bot.restrict_chat_member(message.chat.id,
                                               message.from_user.id,
                                               ChatPermissions(can_send_messages=True,
                                                               can_send_media_messages=True)
                                               )
