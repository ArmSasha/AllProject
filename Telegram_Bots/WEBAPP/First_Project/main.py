from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo


bot = Bot("Тут ваш токен")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.KeyboardButton('open web-app', web_app=WebAppInfo(url='https://sasha108228.github.io/Web_App/')))
	await message.answer('Hi', reply_markup=markup)


executor.start_polling(dp)
