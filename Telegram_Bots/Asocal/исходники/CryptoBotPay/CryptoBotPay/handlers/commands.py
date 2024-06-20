'''https://t.me/AGOMarketBot - Маркет в Telegram'''
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart, ChatTypeFilter

from keyboards.inline.start_kb import start_kb
from utils.db_commands import DataBase


async def start_bot(message: types.Message):
    db = DataBase()
    await db.user.register_user(message.from_user.id)
    user = await db.user.select_user(message.from_user.id)

    await message.answer(
        f'<b>👋 Добро пожаловать в Shop Bot!</b>\n'
        f'<b>🆔:</b> <code>{message.from_user.id}</code>\n'
        f'<b>💵 Баланс:</b> <b>{user.balance} $</b>',
        reply_markup=start_kb
    )


def register_commands(dp: Dispatcher):
    dp.register_message_handler(
        start_bot, ChatTypeFilter(chat_type=types.ChatType.PRIVATE), CommandStart(), state='*'
    )
