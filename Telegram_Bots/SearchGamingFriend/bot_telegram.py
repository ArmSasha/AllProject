from aiogram.utils import executor
from create_bot import dp, bot

from handlers import *


async def on_startup(_):
	print('Бот вышел в онлайн')
	await bot.send_message(1030874842, 'Online')



check_subscribe.register_handlers_check_subscribe(dp)
welcome.register_handlers_welcome(dp)
menu.register_handlers_menu(dp)
games.register_handlers_games(dp)
fortnite.register_handlers_fortnite(dp)
valorant.register_handlers_valorant(dp)
csgo.register_handlers_csgo(dp)
profile.register_handlers_profile(dp)
support.register_handlers_support(dp)



# fortniteSeartchAccounts.register_handlers_fortniteSeartchAccounts(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

