from aiogram import types
from aiogram.dispatcher.filters import CommandStart, ChatTypeFilter
from asyncpg import UniqueViolationError

from loader import dp

from utils import sql_commands

from keyboards import start_kb


@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), CommandStart())
async def start_bot(message: types.Message):
    bot_username = await dp.bot.get_me()
    await message.answer('''
<b>🤖 Что умеет этот бот?</b>
👉 Бот не позволит отправить сообщение участникам чата, пока она не подпишутся на канал или чат.

<b>❗️ Чтобы пользоваться ботом вам необходимо:</b>
<i>1) Добавить его в канал/чат и сделать админом
2) Прописать команду /add (@USERNAME), эта команда позволит установить канал/чат на который надо подписаться, и в этом же канале/чате будет выходить табличка: (@USERNAME), пожалуйста, подпишитесь подпишитесь на наши чаты, чтобы иметь возможность отправлять сообщения в этой группе!
3) Чтобы убрать табличку у пользователей в вашем чате, вам необходимо прописать команду /delete</i>

<b>🤖 Больше ботов: @BarlSoft
🧑‍💻 Кодер: @BarlCoder</b>''',
                         reply_markup=await start_kb(bot_username.username)
                         )
