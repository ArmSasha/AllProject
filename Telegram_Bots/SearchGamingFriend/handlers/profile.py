
from create_bot import dp, bot, db, check_sub_channels
from db import Database
from aiogram import types, Dispatcher
import config as con


from keyboards import profile as nav



#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='profile')
async def profile(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = con.profile(message.from_user.id), photo = Logo, reply_markup=nav.profilebtn)

	# await bot.send_message(message.from_user.id, text=con.profile(message.from_user.id), reply_markup=nav.backMenu)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='profileFortnite')
async def fortniteAccount(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = con.profileFortnite(message.from_user.id), photo = Logo, reply_markup=nav.editProfileFortnite)

	# await bot.send_message(message.from_user.id, text=con.profile(message.from_user.id), reply_markup=nav.backMenu)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='profileFortnite')
async def valorantAccount(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = con.profileValorant(message.from_user.id), photo = Logo, reply_markup=nav.editProfileValorant)

	# await bot.send_message(message.from_user.id, text=con.profile(message.from_user.id), reply_markup=nav.backMenu)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='profileFortnite')
async def CSGOAccount(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = con.profileCSGO(message.from_user.id), photo = Logo, reply_markup=nav.editProfileCSGO)

	# await bot.send_message(message.from_user.id, text=con.profile(message.from_user.id), reply_markup=nav.backMenu)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------


# @dp.callback_query_handler(text='backProfile')
async def backProfile(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = con.profile(message.from_user.id), photo = Logo, reply_markup=nav.profilebtn)

	# await bot.send_message(message.from_user.id, text=con.profile(message.from_user.id), reply_markup=nav.backMenu)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------


#Регистрируем хендлеры
def register_handlers_profile(dp: Dispatcher):
	dp.register_callback_query_handler(profile, text='profile')
	dp.register_callback_query_handler(backProfile, text='backProfile')
	dp.register_callback_query_handler(fortniteAccount, text='fortniteAccount')
	dp.register_callback_query_handler(valorantAccount, text='valorantAccount')
	dp.register_callback_query_handler(CSGOAccount, text='csgoAccount')


