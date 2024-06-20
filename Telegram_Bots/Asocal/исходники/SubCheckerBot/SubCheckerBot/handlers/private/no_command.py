from aiogram import types
from aiogram.dispatcher.filters import ChatTypeFilter

from keyboards import start_kb
from loader import dp


@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE))
async def no_command(message: types.Message):
    bot_username = await dp.bot.get_me()
    await message.reply('<b>🤖 К сожалению, я не понимаю вас!</b>\n'
                        '<b>👇 Воспользуйтесь меню</b>',
                        reply_markup=await start_kb(bot_username.username)
                        )
