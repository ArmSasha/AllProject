import logging
from aiogram import Bot, Dispatcher, types
import os


API_TOKEN = '6535764478:AAFb3ag-2IPOvS4teLkGOV-hKtQoRNd_H2g'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
	await message.reply("Запуск")
	os.startfile('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/ParserUL_bot/main.py')

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
