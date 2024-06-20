from aiogram.utils import executor
from create_bot import dp

from handlers import condition, client, bot_mailing, bot_support


async def on_startup(_):
	print('Бот вышел в онлайн')

bot_mailing.register_handlers_bot_mailing(dp)
condition.register_handlers_condition(dp)
client.register_handlers_client(dp)
bot_support.register_handlers_bot_support(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)