from create_bot import dp, bot, db, check_sub_channels
from db import Database
from aiogram import types, Dispatcher
import config as con
from keyboards import games as nav
from keyboards import menu as navs
from keyboards import fortnite as btn
from keyboards import valorant as vl
from keyboards import csgo as cs

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='fortnite')
async def fortnite(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'Выберите режим:', photo = Logo, reply_markup=nav.fortnitebtn)


	# await bot.send_message(message.from_user.id, 'Выберите режим:', reply_markup=nav.fortnitebtn)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='fortnite_arena')
async def arenaFortnite(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'fortnite_arena', photo = Logo, reply_markup=btn.forniteStart)

	# await bot.send_message(message.from_user.id, 'fortnite_arena', reply_markup=nav.backFortnite)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='prakiFortnite')
async def prakiFortnite(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'prakiFortnite', photo = Logo, reply_markup=btn.forniteStart)

	# await bot.send_message(message.from_user.id, 'fortnite_arena', reply_markup=nav.backFortnite)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='fortnite_tournament')
async def tournamentFortnite(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'fortnite_tournament', photo = Logo, reply_markup=btn.forniteStart)

	# await bot.send_message(message.from_user.id, 'fortnite_tournament', reply_markup=nav.backFortnite)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='PGFortnite')
async def PGFortnite(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'PGFortnite', photo = Logo, reply_markup=btn.forniteStart)

	# await bot.send_message(message.from_user.id, 'fortnite_tournament', reply_markup=nav.backFortnite)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='valorant')
async def valorant(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'Выберите режим:', photo = Logo, reply_markup=vl.ValorantStart)

	# await bot.send_message(message.from_user.id, 'Выберите режим:', reply_markup=nav.valorantbtn)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='valorant_rating')
async def ratingValorant(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'ratingValorant', photo = Logo, reply_markup=vl.ValorantStart)

	# await bot.send_message(message.from_user.id, 'valorant_rating', reply_markup=nav.backValorant)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='pablickValorant')
async def pablickValorant(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'pablickValorant', photo = Logo, reply_markup=vl.ValorantStart)

	# await bot.send_message(message.from_user.id, 'valorant_premier', reply_markup=nav.backValorant)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
# @dp.callback_query_handler(text='premierValorant')
async def premierValorant(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'premierValorant', photo = Logo, reply_markup=vl.ValorantStart)

	# await bot.send_message(message.from_user.id, 'valorant_rating', reply_markup=nav.backValorant)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='prakiValorant')
async def prakiValorant(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'prakiValorant', photo = Logo, reply_markup=vl.ValorantStart)

	# await bot.send_message(message.from_user.id, 'valorant_premier', reply_markup=nav.backValorant)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='dota')
async def dota(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'Выберите режим:', photo = Logo, reply_markup=nav.dotabtn)

	# await bot.send_message(message.from_user.id, 'Выберите режим:', reply_markup=nav.dotabtn)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
# @dp.callback_query_handler(text='ratingDota')
async def ratingDota(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'ratingDota', photo = Logo, reply_markup=nav.backDota)

	# await bot.send_message(message.from_user.id, 'ratingDota', reply_markup=nav.backDota)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='pablickDota')
async def pablickDota(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'pablickDota', photo = Logo, reply_markup=nav.backDota)

	# await bot.send_message(message.from_user.id, 'premierDota', reply_markup=nav.backDota)


#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='tournamentDota')
async def turboDota(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'turboDota', photo = Logo, reply_markup=nav.backDota)

	# await bot.send_message(message.from_user.id, 'ratingDota', reply_markup=nav.backDota)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='CSGO')
async def csgo(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'Выберите режим:', photo = Logo, reply_markup=nav.csgobtn)

	# await bot.send_message(message.from_user.id, 'Выберите режим:', reply_markup=nav.csgobtn)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='faceitCSGO')
async def faceitCSGO(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'faceitCSGO', photo = Logo, reply_markup=cs.CSGOStart)


	# await bot.send_message(message.from_user.id, 'faceitCSGO', reply_markup=nav.backCSGO)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='ratingCSGO')
async def ratingCSGO(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'ratingCSGO', photo = Logo, reply_markup=cs.CSGOStart)


	# await bot.send_message(message.from_user.id, 'tournamentCSGO', reply_markup=nav.backCSGO)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='prakiCSGO')
async def prakiCSGO(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'prakiCSGO', photo = Logo, reply_markup=cs.CSGOStart)


	# await bot.send_message(message.from_user.id, 'faceitCSGO', reply_markup=nav.backCSGO)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='tournamentCSGO')
async def OnexOneCSGO(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'OnexOneCSGO', photo = Logo, reply_markup=cs.CSGOStart)


	# await bot.send_message(message.from_user.id, 'tournamentCSGO', reply_markup=nav.backCSGO)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='backGame')
async def backGame(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'Выберите игру: ', photo = Logo, reply_markup=navs.gamesMenu)


	# await bot.send_message(message.from_user.id, 'Выберите игру: ', reply_markup=navs.gamesMenu)

# @dp.callback_query_handler(text='backFortnite')
async def backFortnite(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'Выберите режим: ', photo = Logo, reply_markup=nav.fortnitebtn)


	# await bot.send_message(message.from_user.id, 'Выберите режим: ', reply_markup=nav.fortnitebtn)

# @dp.callback_query_handler(text='backValorant')
async def backValorant(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'Выберите режим: ', photo = Logo, reply_markup=nav.valorantbtn)

	# await bot.send_message(message.from_user.id, 'Выберите режим: ', reply_markup=nav.valorantbtn)

# @dp.callback_query_handler(text='backDota')
async def backDota(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'Выберите режим: ', photo = Logo, reply_markup=nav.dotabtn)

	# await bot.send_message(message.from_user.id, 'Выберите режим: ', reply_markup=nav.dotabtn)

# @dp.callback_query_handler(text='backCSGO')
async def backCSGO(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
	await bot.send_photo(message.from_user.id, caption = 'Выберите режим: ', photo = Logo, reply_markup=nav.csgobtn)


	# await bot.send_message(message.from_user.id, 'Выберите режим: ', reply_markup=nav.csgobtn)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

#Регистрируем хендлеры
def register_handlers_games(dp: Dispatcher):
	dp.register_callback_query_handler(fortnite, text='fortnite')
	dp.register_callback_query_handler(arenaFortnite, text='arenaFortnite')
	dp.register_callback_query_handler(prakiFortnite, text='prakiFortnite')
	dp.register_callback_query_handler(tournamentFortnite, text='tournamentFortnite')
	dp.register_callback_query_handler(PGFortnite, text='PGFortnite')
#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(valorant, text='valorant')
	dp.register_callback_query_handler(ratingValorant, text='ratingValorant')
	dp.register_callback_query_handler(pablickValorant, text='pablickValorant')
	dp.register_callback_query_handler(premierValorant, text='premierValorant')
	dp.register_callback_query_handler(prakiValorant, text='prakiValorant')
#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(dota, text='dota')
	dp.register_callback_query_handler(ratingDota, text='ratingDota')
	dp.register_callback_query_handler(pablickDota, text='pablickDota')
	dp.register_callback_query_handler(turboDota, text='turboDota')
#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(csgo, text='csgo')
	dp.register_callback_query_handler(faceitCSGO, text='faceitCSGO')
	dp.register_callback_query_handler(ratingCSGO, text='ratingCSGO')
	dp.register_callback_query_handler(prakiCSGO, text='prakiCSGO')
	dp.register_callback_query_handler(OnexOneCSGO, text='OnexOneCSGO')
#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(backGame, text='backGame')
#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(backFortnite, text='backFortnite')
#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(backValorant, text='backValorant')
#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(backDota, text='backDota')
#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(backCSGO, text='backCSGO')
#----------------------------------------------------------------------------------------------------------------
