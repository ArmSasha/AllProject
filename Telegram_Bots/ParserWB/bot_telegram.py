from aiogram.utils import executor
from create_bot import dp, bot

from handlers import *


async def on_startup(_):
	print('Бот вышел в онлайн')
	await bot.send_message(1030874842, 'Online')

main.register_handlers_main(dp)
# condition.register_handlers_condition(dp)
# client.register_handlers_client(dp)
# bot_support.register_handlers_bot_support(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)