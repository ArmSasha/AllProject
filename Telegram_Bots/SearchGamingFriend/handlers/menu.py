from create_bot import dp, bot, db, check_sub_channels
from db import Database
from aiogram import types, Dispatcher
import config as con
from keyboards import menu as nav



#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='games')
async def games(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'Please click button', photo = Logo, reply_markup=nav.gamesMenu)



	# await bot.send_message(message.from_user.id, 'Выберите игру: ', reply_markup=nav.gamesMenu)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='backMenu')
async def backMenu(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'Please click button', photo = Logo, reply_markup=nav.mainMenu)


	# await bot.send_message(message.from_user.id, "Please click button", reply_markup=nav.mainMenu)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

#Регистрируем хендлеры
def register_handlers_menu(dp: Dispatcher):
	dp.register_callback_query_handler(games, text='games')
	dp.register_callback_query_handler(backMenu, text='backMenu')
