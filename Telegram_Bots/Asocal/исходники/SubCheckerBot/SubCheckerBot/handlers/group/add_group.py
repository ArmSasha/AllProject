from aiogram import types
from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram.utils.exceptions import BotKicked, ChatNotFound
from asyncpg import UniqueViolationError

from loader import dp
from utils.db_api import sql_commands


@dp.message_handler(ChatTypeFilter(chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP]), text_startswith='/add')
async def add_command(message: types.Message):
    try:
        try:
            try:
                chat = message.text.split(' ')[1]
                user_info = await dp.bot.get_chat_member(chat, message.from_user.id)
                if user_info.status == 'creator' or user_info.status == 'administrator':
                    bot_id = await dp.bot.get_me()
                    is_bot_in_chat = await dp.bot.get_chat_member(chat, bot_id.id)
                    if is_bot_in_chat.status == 'left':
                        await message.reply('<b>❗️ Бот отсутствует в данном чате!</b>')
                    elif is_bot_in_chat.status == 'administrator':
                        try:
                            chat_info = await dp.bot.get_chat(chat)
                            await sql_commands.add_group(message.chat.id, chat_info.id,
                                                         chat_info.title, f'https://t.me/{chat_info.username}')
                            await message.reply('<b>🎉 Чат был успешно добавлен!</b>')
                        except UniqueViolationError:
                            await message.reply('<b>❗️ Чат уже добавлен!</b>')
                    else:
                        await message.reply('<b>❗️ Бот не является администратором данного чата!</b>')
                else:
                    await message.reply('<b>❗️ Вы не являетесь администратором данного чата!</b>')
            except BotKicked:
                await message.reply('<b>❗️ Бот заблокирован в данном чате!</b>')
        except ChatNotFound:
            await message.reply('<b>❗️ Такого чата не существует!</b>')
    except IndexError:
        await message.reply('<b>❗️ Необходимо ввести 1 аргумент для этой команды!</b>')
