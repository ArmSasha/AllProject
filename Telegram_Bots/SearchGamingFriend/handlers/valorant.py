from create_bot import dp, bot, db, check_sub_channels
from db import Database
from aiogram import types, Dispatcher
import config as con
from keyboards import check_subscribe_btn as navs
from keyboards import menu as nav
from keyboards import valorant as btn
from states import FSMValorant
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


# @dp.callback_query_handler(text='createFortniteAccount', , state = None)
async def createValorantAccount(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	if(not db.user_exists_valorant(message.from_user.id)):
		if await check_sub_channels(con.CHANNELS, message.from_user.id):
			db.add_user_valorant(message.from_user.id)
			await FSMValorant.kd.set()
			await bot.send_message(message.from_user.id, 'Заполнение анкеты📝:')
			await bot.send_message(message.from_user.id, 'Укажите ваше KD, как указано в примере: "0,53"')
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
async def editProfileValorant(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	if await check_sub_channels(con.CHANNELS, message.from_user.id):
		if(not db.get_block(message.from_user.id)):
			await FSMValorant.kd.set()
			await bot.send_message(message.from_user.id, 'Заполнение анкеты📝:')
			await bot.send_message(message.from_user.id, 'Укажите ваше KD, как указано в примере: "0,53"')
		else:
			await bot.send_message(message.from_user.id, con.NOT_SUB_MESSAGE, reply_markup=navs.showChannels())
	else:
		await bot.send_message(message.from_user.id, "Вы заблокированы!")

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.message_handler(state=FSMValorant.kd)
async def load_kd(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['kd'] = message.text
		db.set_kd_valorant(message.from_user.id, message.text)
		await message.answer('Укажите ранг', reply_markup = btn.rank)
		await FSMValorant.next()

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMValorant.role)
async def load_rank_Iron(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Iron'
		db.set_rank_valorant(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMValorant.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMValorant.role)
async def load_rank_Bronze(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Bronze'
		db.set_rank_valorant(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMValorant.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMValorant.role)
async def load_rank_Silver(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Silver'
		db.set_rank_valorant(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMValorant.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMValorant.role)
async def load_rank_Gold(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Gold'
		db.set_rank_valorant(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMValorant.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMValorant.role)
async def load_rank_Platinum(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Platinum'
		db.set_rank_valorant(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMValorant.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMValorant.role)
async def load_rank_Diamond(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Diamond'
		db.set_rank_valorant(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMValorant.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMValorant.role)
async def load_rank_Elite(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Ascendant'
		db.set_rank_valorant(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMValorant.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMValorant.role)
async def load_rank_Champion(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Immortal'
		db.set_rank_valorant(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMValorant.next()

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.message_handler(state=FSMValorant.description)
async def load_description(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['description'] = message.text
		db.set_description_valorant(message.from_user.id, data['description'])
		await bot.send_message(message.from_user.id, 'Анкета заполнена, удачного пользования!', reply_markup = nav.mainMenu)
		await state.finish()

#----------------------------------------------------------------------------------------------------------------

#Регистрируем хендлеры
def register_handlers_valorant(dp: Dispatcher):
	dp.register_callback_query_handler(createValorantAccount, text='createValorantAccount', state = None)
	dp.register_callback_query_handler(editProfileValorant, text='editProfileValorant', state = None)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_message_handler(load_kd, state=FSMValorant.kd)
	#----------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Iron, text='IronValorant', state=FSMValorant.rank)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Bronze, text='BronzeValorant', state=FSMValorant.rank)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Silver, text='SilverValorant', state=FSMValorant.rank)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Gold, text='GoldValorant', state=FSMValorant.rank)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Platinum, text='PlatinumValorant', state=FSMValorant.rank)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Diamond, text='DiamondValorant', state=FSMValorant.rank)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Elite, text='AscendantValorant', state=FSMValorant.rank)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Champion, text='ImmortalValorant', state=FSMValorant.rank)
	#----------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------------------------------------------------------
	dp.register_message_handler(load_description, state=FSMValorant.description)
	#----------------------------------------------------------------------------------------------------------------

