from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ParseMode


bot = Bot('5714593221:AAE_vzYtjwfa0h7RlDO4scezpxsGQYIDWCg')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("<b><pre><code style='color:red'>Красный текст</code></pre></b>", parse_mode=ParseMode.HTML)

if __name__ == '__main__':
    executor.start_polling(dp)