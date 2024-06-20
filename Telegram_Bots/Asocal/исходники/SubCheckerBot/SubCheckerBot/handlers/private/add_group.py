from aiogram import types
from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), Command('add'))
async def add_command(message: types.Message):
    await message.reply('<b>❗️ Данная команда достуна только в групповых чатах!</b>')

