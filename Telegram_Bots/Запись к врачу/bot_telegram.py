from aiogram.utils import executor
from create_bot import dp, bot

from handlers import *


async def on_startup(_):
	print('Бот вышел в онлайн')
	await bot.send_message(1030874842, 'Online')

welcome.register_handlers_welcome(dp)
menu.register_handlers_menu(dp)
doctors.register_handlers_doctors(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

