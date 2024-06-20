from aiogram import types
from aiogram.dispatcher.filters import ChatTypeFilter

from loader import dp
from utils.db_api import sql_commands


@dp.message_handler(ChatTypeFilter(chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP]), text='/delete')
async def delete_groups(message: types.Message):
    try:
        user_info = await dp.bot.get_chat_member(message.chat.id, message.from_user.id)
        if user_info.status == 'creator' or user_info.status == 'administrator':
            await sql_commands.delete_all_groups(message.chat.id)
            await message.reply('<b>❌ Все чаты были успешно удалены!</b>')
        else:
            await message.reply('<b>❗️ Вы не являетесь администратором данного чата!</b>')
    except IndexError:
        await message.reply('<b>❗️ Необходимо ввести 1 аргумент для этой команды!</b>')

