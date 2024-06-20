from aiogram import types
from aiogram.types import ChatPermissions

from loader import dp
from utils.db_api import sql_commands


@dp.callback_query_handler(text_startswith='check_sub|')
async def check_sub_member(call: types.CallbackQuery):
    user_id = call.data.split('|')[1]
    if int(user_id) == call.from_user.id:
        subscribed = 0
        groups = await sql_commands.select_group(call.message.chat.id)
        for group in groups:
            sub = await dp.bot.get_chat_member(group["group_id"], user_id)
            if sub.status != types.ChatMemberStatus.LEFT:
                subscribed += 1
            else:
                await call.answer('❗️ Вы не подписались на чаты!',
                                  show_alert=True)
        else:
            if subscribed == len(groups):
                await call.answer('✅ Вы успешно прошли проверку!',
                                  show_alert=True)
                await call.message.delete()
                await call.message.bot.restrict_chat_member(call.message.chat.id,
                                                            call.from_user.id,
                                                            ChatPermissions(can_send_messages=True,
                                                                            can_send_media_messages=True)
                                                            )
    else:
        await call.answer('❗️ Данный опрос создан для другого участника чата!',
                          show_alert=True)
