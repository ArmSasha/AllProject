from create_bot import dp, bot, db, check_sub_channels
from db import Database
from aiogram import types, Dispatcher
import config as con
from keyboards import check_subscribe_btn as navs
from keyboards import menu as nav
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboards import csgo as btn
from states import FSMCSGO

# @dp.callback_query_handler(text='createFortniteAccount', , state = None)
async def createCSGOAccount(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	if(not db.user_exists_csgo(message.from_user.id)):
		if await check_sub_channels(con.CHANNELS, message.from_user.id):
			db.add_user_csgo(message.from_user.id)
			await FSMCSGO.faceit.set()
			await bot.send_message(message.from_user.id, 'Заполнение анкеты📝:')
			await bot.send_message(message.from_user.id, 'Укажите уровень фейсита', reply_markup = btn.faceitbtn)
		else:
			await bot.send_message(message.from_user.id, con.NOT_SUB_MESSAGE, reply_markup=navs.showChannels())
	else:
		if(not db.get_block(message.from_user.id)):
			Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
			await bot.send_photo(message.from_user.id, caption = 'Выберите категорию:', photo = Logo, reply_markup=nav.mainMenu)
			await bot.send_message(message.from_user.id, "Аккаунт уже создан")

		else:
			await bot.send_message(message.from_user.id, "Вы заблокированы!")

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='editProfileFortnite', , state = None)
async def editProfileCSGO(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	if await check_sub_channels(con.CHANNELS, message.from_user.id):
		if(not db.get_block(message.from_user.id)):
			await FSMCSGO.faceit.set()
			await bot.send_message(message.from_user.id, 'Заполнение анкеты📝:')
			await bot.send_message(message.from_user.id, 'Укажите уровень фейсита', reply_markup = btn.faceitbtn)
		else:
			await bot.send_message(message.from_user.id, con.NOT_SUB_MESSAGE, reply_markup=navs.showChannels())
	else:
		await bot.send_message(message.from_user.id, "Вы заблокированы!")


#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMCSGO.role)
async def load_faceit_lvl1(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['faceit'] = 'LVL 1'
		db.set_faceit_csgo(callback_query.from_user.id, data['faceit'])
		await bot.send_message(callback_query.from_user.id, 'Укажите ваш ранг', reply_markup = btn.rankbtn)
		await bot.answer_callback_query(callback_query.id)
		await FSMCSGO.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMCSGO.role)
async def load_faceit_lvl2(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['faceit'] = 'LVL 2'
		db.set_faceit_csgo(callback_query.from_user.id, data['faceit'])
		await bot.send_message(callback_query.from_user.id, 'Укажите ваш ранг', reply_markup = btn.rankbtn)
		await bot.answer_callback_query(callback_query.id)
		await FSMCSGO.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMCSGO.role)
async def load_faceit_lvl3(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['faceit'] = 'LVL 3'
		db.set_faceit_csgo(callback_query.from_user.id, data['faceit'])
		await bot.send_message(callback_query.from_user.id, 'Укажите ваш ранг', reply_markup = btn.rankbtn)
		await bot.answer_callback_query(callback_query.id)
		await FSMCSGO.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMCSGO.role)
async def load_faceit_lvl4(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['faceit'] = 'LVL 4'
		db.set_faceit_csgo(callback_query.from_user.id, data['faceit'])
		await bot.send_message(callback_query.from_user.id, 'Укажите ваш ранг', reply_markup = btn.rankbtn)
		await bot.answer_callback_query(callback_query.id)
		await FSMCSGO.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMCSGO.role)
async def load_faceit_lvl5(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['faceit'] = 'LVL 5'
		db.set_faceit_csgo(callback_query.from_user.id, data['faceit'])
		await bot.send_message(callback_query.from_user.id, 'Укажите ваш ранг', reply_markup = btn.rankbtn)
		await bot.answer_callback_query(callback_query.id)
		await FSMCSGO.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMCSGO.role)
async def load_faceit_lvl6(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['faceit'] = 'LVL 6'
		db.set_faceit_csgo(callback_query.from_user.id, data['faceit'])
		await bot.send_message(callback_query.from_user.id, 'Укажите ваш ранг', reply_markup = btn.rankbtn)
		await bot.answer_callback_query(callback_query.id)
		await FSMCSGO.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMCSGO.role)
async def load_faceit_lvl7(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['faceit'] = 'LVL 7'
		db.set_faceit_csgo(callback_query.from_user.id, data['faceit'])
		await bot.send_message(callback_query.from_user.id, 'Укажите ваш ранг', reply_markup = btn.rankbtn)
		await bot.answer_callback_query(callback_query.id)
		await FSMCSGO.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMCSGO.role)
async def load_faceit_lvl8(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['faceit'] = 'LVL 8'
		db.set_faceit_csgo(callback_query.from_user.id, data['faceit'])
		await bot.send_message(callback_query.from_user.id, 'Укажите ваш ранг', reply_markup = btn.rankbtn)
		await bot.answer_callback_query(callback_query.id)
		await FSMCSGO.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMCSGO.role)
async def load_faceit_lvl9(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['faceit'] = 'LVL 9'
		db.set_faceit_csgo(callback_query.from_user.id, data['faceit'])
		await bot.send_message(callback_query.from_user.id, 'Укажите ваш ранг', reply_markup = btn.rankbtn)
		await bot.answer_callback_query(callback_query.id)
		await FSMCSGO.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMCSGO.role)
async def load_faceit_lvl10(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['faceit'] = 'LVL 10'
		db.set_faceit_csgo(callback_query.from_user.id, data['faceit'])
		await bot.send_message(callback_query.from_user.id, 'Укажите ваш ранг', reply_markup = btn.rankbtn)
		await bot.answer_callback_query(callback_query.id)
		await FSMCSGO.next()

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMCSGO.role)
async def load_rank_Silver(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		await bot.send_message(callback_query.from_user.id, 'Уточните ранг', reply_markup = btn.Silverbtn)
		await bot.answer_callback_query(callback_query.id)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Silver1', state=FSMCSGO.role)
async def load_rank_Silver1(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Silver 1'
		db.set_rank_csgo(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMCSGO.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Silver1', state=FSMCSGO.role)
async def load_rank_Silver2(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Silver 2'
		db.set_rank_csgo(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMCSGO.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Silver1', state=FSMCSGO.role)
async def load_rank_Silver3(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Silver 3'
		db.set_rank_csgo(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMCSGO.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Silver1', state=FSMCSGO.role)
async def load_rank_Silver4(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Silver 4'
		db.set_rank_csgo(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMCSGO.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Silver1', state=FSMCSGO.role)
async def load_rank_Silver5(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Silver 5'
		db.set_rank_csgo(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMCSGO.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Silver1', state=FSMCSGO.role)
async def load_rank_Silver_Elit_Master(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Silver Elit Master'
		db.set_rank_csgo(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMCSGO.next()

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMCSGO.role)
async def load_rank_Goldnova(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Goldnova'
		db.set_rank_csgo(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Уточните ранг', reply_markup = btn.Goldnovabtn)
		await bot.answer_callback_query(callback_query.id)

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Silver1', state=FSMCSGO.role)
async def load_rank_Goldnova1(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Gold Nova I'
		db.set_rank_csgo(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMCSGO.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Silver1', state=FSMCSGO.role)
async def load_rank_Goldnova2(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Gold Nova II'
		db.set_rank_csgo(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMCSGO.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Silver1', state=FSMCSGO.role)
async def load_rank_Goldnova3(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Gold Nova III'
		db.set_rank_csgo(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMCSGO.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Silver1', state=FSMCSGO.role)
async def load_rank_GoldNova_Master(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Gold Nova Master'
		db.set_rank_csgo(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMCSGO.next()

#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMCSGO.role)
async def load_rank_Kalash(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Kalash'
		db.set_rank_csgo(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Уточните ранг', reply_markup = btn.Kalashbtn)
		await bot.answer_callback_query(callback_query.id)

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Silver1', state=FSMCSGO.role)
async def load_rank_Kalash1(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Master Guardian I'
		db.set_rank_csgo(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMCSGO.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Silver1', state=FSMCSGO.role)
async def load_rank_Kalash2(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Master Guardian II'
		db.set_rank_csgo(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMCSGO.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Silver1', state=FSMCSGO.role)
async def load_rank_Kalash3(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Master Guardian Elite'
		db.set_rank_csgo(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMCSGO.next()

#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMCSGO.role)
async def load_rank_Bigstar(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Bigstar'
		db.set_rank_csgo(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMCSGO.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMCSGO.role)
async def load_rank_Golden_Eagle(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Golden Eagle'
		db.set_rank_csgo(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Уточните ранг', reply_markup = btn.Golden_Eagle_btn)
		await bot.answer_callback_query(callback_query.id)

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Silver1', state=FSMCSGO.role)
async def load_rank_Golden_Eagle1(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Legendary Eagle'
		db.set_rank_csgo(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMCSGO.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Silver1', state=FSMCSGO.role)
async def load_rank_Golden_Eagle2(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Legendary Eagle Master'
		db.set_rank_csgo(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMCSGO.next()

#----------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMCSGO.role)
async def load_rank_Supreme(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Supreme'
		db.set_faceit_csgo(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMCSGO.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='GlobalCSGO', state=FSMCSGO.role)
async def load_rank_Global(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Global'
		db.set_faceit_csgo(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMCSGO.next()

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.message_handler(state=FSMCSGO.description)
async def load_description(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['description'] = message.text
		db.set_description_csgo(message.from_user.id, data['description'])
		await bot.send_message(message.from_user.id, 'Анкета заполнена, удачного пользования!', reply_markup = nav.mainMenu)
		await state.finish()

#----------------------------------------------------------------------------------------------------------------

#Регистрируем хендлеры
def register_handlers_csgo(dp: Dispatcher):
	dp.register_callback_query_handler(createCSGOAccount, text='createCSGOAccount', state = None)
	dp.register_callback_query_handler(editProfileCSGO, text='editProfileCSGO', state = None)
	#----------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_faceit_lvl1, text='lvl1', state=FSMCSGO.faceit)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_faceit_lvl2, text='lvl2', state=FSMCSGO.faceit)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_faceit_lvl3, text='lvl3', state=FSMCSGO.faceit)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_faceit_lvl4, text='lvl4', state=FSMCSGO.faceit)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_faceit_lvl5, text='lvl5', state=FSMCSGO.faceit)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_faceit_lvl6, text='lvl6', state=FSMCSGO.faceit)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_faceit_lvl7, text='lvl7', state=FSMCSGO.faceit)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_faceit_lvl8, text='lvl8', state=FSMCSGO.faceit)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_faceit_lvl9, text='lvl9', state=FSMCSGO.faceit)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_faceit_lvl10, text='lvl10', state=FSMCSGO.faceit)
	#----------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Silver, text='SilverCSGO', state=FSMCSGO.rank)
	#----------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Silver1, text='Silver1', state=FSMCSGO.rank)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Silver2, text='Silver2', state=FSMCSGO.rank)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Silver3, text='Silver3', state=FSMCSGO.rank)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Silver4, text='Silver4', state=FSMCSGO.rank)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Silver5, text='Silver5', state=FSMCSGO.rank)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Silver_Elit_Master, text='Silver_Elit_Master', state=FSMCSGO.rank)
	#----------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Goldnova, text='GoldnovaCSGO', state=FSMCSGO.rank)
	#----------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Goldnova1, text='Goldnova1', state=FSMCSGO.rank)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Goldnova2, text='Goldnova2', state=FSMCSGO.rank)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Goldnova3, text='Goldnova3', state=FSMCSGO.rank)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_GoldNova_Master, text='GoldNova_Master', state=FSMCSGO.rank)
	#----------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Kalash, text='KalashCSGO', state=FSMCSGO.rank)
	#----------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Kalash1, text='Kalash1', state=FSMCSGO.rank)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Kalash2, text='Kalash2', state=FSMCSGO.rank)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Kalash3, text='Kalash3', state=FSMCSGO.rank)
	#----------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Bigstar, text='BigstarCSGO', state=FSMCSGO.rank)
	#----------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Golden_Eagle, text='Golden_EagleCSGO', state=FSMCSGO.rank)
	#----------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Golden_Eagle1, text='Golden_Eagle1', state=FSMCSGO.rank)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Golden_Eagle2, text='Golden_Eagle2', state=FSMCSGO.rank)
	#----------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Supreme, text='SupremeCSGO', state=FSMCSGO.rank)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Global, text='GlobalCSGO', state=FSMCSGO.rank)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_message_handler(load_description, state=FSMCSGO.description)
	#----------------------------------------------------------------------------------------------------------------

