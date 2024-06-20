from create_bot import dp, bot, db, check_sub_channels
from db import Database
from aiogram import Bot, types, Dispatcher, executor
import config as con
from keyboards import check_subscribe_btn as navs
from keyboards import menu as nav
from keyboards import fortnite as btn
from states import FSMFortnite
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import exceptions

# # @dp.callback_query_handler(text='forniteSearchAccounts')
# async def forniteSearchAccounts(message: types.Message):
#     # Отправляем первую страницу с пользователями
#     await update_user_info(message)




users_per_page = 3
current_index = {}
current_message_id = {}

# Функция для получения пользователей из базы данных
def get_users(offset):
    rows = db.get_people_fortnite(users_per_page, offset)
    return rows if rows else []

# Функция для форматирования данных пользователей
def format_users(users):
    global current_message_id
    formatted_data = []
    for user in users:
        name, age, kd, pr, role, description = user
        formatted_row = f"Имя: {name} \n Возраст: {age} \n KD: {kd} \n PR: {pr} \n Role: {role} \n Описание: {description}"
        formatted_data.append(formatted_row)

    response = '\n ____________________ \n'.join(formatted_data)
    return response

# Обработчик команды /start
# @dp.message_handler(commands=['start'])
async def forniteSearchAccounts(message: types.Message):
    user_id = message.from_user.id
    current_index[user_id] = 0
    global current_message_id

    offset = current_index[user_id] * users_per_page
    users = get_users(offset)

    response = ""
    if users:
        response = format_users(users)
    else:
        response = "Нет данных о пользователях."

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    if len(users) == users_per_page:
        next_button = types.InlineKeyboardButton("Дальше", callback_data="next")
        keyboard.add(next_button)

    sent_message = await bot.send_message(message.from_user.id, text=response, reply_markup=keyboard)
    current_message_id[user_id] = sent_message.message_id

# Обработчик нажатия на кнопку "Дальше"
# @dp.callback_query_handler(text="next")
async def next_person(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    global current_message_id

    # Удаление предыдущего сообщения
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=current_message_id[user_id])

    # Получение следующих трех пользователей из базы данных
    current_index[user_id] += 1
    offset = current_index[user_id] * users_per_page
    users = get_users(offset)

    # Форматирование данных для вывода
    response = format_users(users)

    # Создание клавиатуры с кнопкой "Назад"
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    prev_button = types.InlineKeyboardButton("Назад", callback_data="prev")
    keyboard.add(prev_button)

    sent_message = await bot.send_message(chat_id=callback_query.message.chat.id, text=response, reply_markup=keyboard)
    current_message_id[user_id] = sent_message.message_id

# Обработчик нажатия на кнопку "Назад"
# @dp.callback_query_handler(text="prev")
async def prev_person(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    global current_message_id

    # Удаление предыдущего сообщения
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=current_message_id[user_id])

    # Получение предыдущих трех пользователей из базы данных
    current_index[user_id] -= 1
    offset = current_index[user_id] * users_per_page
    users = get_users(offset)

    # Форматирование данных для вывода
    response = format_users(users)

    # Создание клавиатуры с кнопкой "Дальше"
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    next_button = types.InlineKeyboardButton("Дальше", callback_data="next")
    keyboard.add(next_button)

    sent_message = await bot.send_message(chat_id=callback_query.message.chat.id, text=response, reply_markup=keyboard)
    current_message_id[user_id] = sent_message.message_id





#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='createFortniteAccount', , state = None)
async def createFortniteAccount(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)

	if(not db.user_exists_fortnite(message.from_user.id)):
		if await check_sub_channels(con.CHANNELS, message.from_user.id):
			db.add_user_fortnite(message.from_user.id)
			await FSMFortnite.kd.set()
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
async def editProfileFortnite(message: types.Message):
	await bot.delete_message(message.from_user.id, message.message.message_id)
	if(not db.get_block(message.from_user.id)):
		if(not db.user_exists_fortnite(message.from_user.id)):
			if await check_sub_channels(con.CHANNELS, message.from_user.id):
				db.add_user_fortnite(message.from_user.id)
				await FSMFortnite.kd.set()
				await bot.send_message(message.from_user.id, 'Заполнение анкеты📝:')
				await bot.send_message(message.from_user.id, 'Укажите ваше KD, как указано в примере: "0,53"')
			else:
				await bot.send_message(message.from_user.id, con.NOT_SUB_MESSAGE, reply_markup=navs.showChannels())
		else:
			if(not db.get_block(message.from_user.id)):
				await FSMFortnite.kd.set()
				await bot.send_message(message.from_user.id, 'Заполнение анкеты📝:')
				await bot.send_message(message.from_user.id, 'Укажите ваше KD, как указано в примере: "0,53"')

	else:
		await bot.send_message(message.from_user.id, "Вы заблокированы!")


#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.message_handler(state=FSMFortnite.kd)
async def load_kd(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['kd'] = message.text
		db.set_kd_fortnite(message.from_user.id, message.text)
		await message.answer('Введите PR')
		await FSMFortnite.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.message_handler(state=FSMFortnite.pr)
async def load_pr(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['pr'] = message.text
		db.set_pr_fortnite(message.from_user.id, message.text)
		await message.answer('Выберите свою роль', reply_markup=btn.rolebtn)
		await FSMFortnite.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='IGL', state=FSMFortnite.role)
async def load_role_IGL(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['role'] = 'IGL (In game leader)'
		db.set_role_fortnite(callback_query.from_user.id, data['role'])
		await bot.send_message(callback_query.from_user.id, 'Укажите свой ранг', reply_markup = btn.rankbtn)
		await bot.answer_callback_query(callback_query.id)
		await FSMFortnite.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Fragger', state=FSMFortnite.role)
async def load_role_Fragger(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['role'] = 'Fragger'
		db.set_role_fortnite(callback_query.from_user.id, data['role'])
		await bot.send_message(callback_query.from_user.id, 'Укажите свой ранг', reply_markup = btn.rankbtn)
		await bot.answer_callback_query(callback_query.id)
		await FSMFortnite.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMFortnite.role)
async def load_role_Support(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['role'] = 'Support'
		db.set_role_fortnite(callback_query.from_user.id, data['role'])
		await bot.send_message(callback_query.from_user.id, 'Укажите свой ранг', reply_markup = btn.rankbtn)
		await bot.answer_callback_query(callback_query.id)
		await FSMFortnite.next()

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMFortnite.role)
async def load_rank_Bronze(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Bronze'
		db.set_rank_fortnite(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMFortnite.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMFortnite.role)
async def load_rank_Silver(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Silver'
		db.set_rank_fortnite(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMFortnite.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMFortnite.role)
async def load_rank_Gold(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Gold'
		db.set_rank_fortnite(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMFortnite.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMFortnite.role)
async def load_rank_Platinum(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Platinum'
		db.set_rank_fortnite(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMFortnite.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMFortnite.role)
async def load_rank_Diamond(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Diamond'
		db.set_rank_fortnite(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMFortnite.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMFortnite.role)
async def load_rank_Elite(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Elite'
		db.set_rank_fortnite(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMFortnite.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMFortnite.role)
async def load_rank_Champion(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Champion'
		db.set_rank_fortnite(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMFortnite.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='Support', state=FSMFortnite.role)
async def load_rank_Unreal(callback_query: types.CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		data['rank'] = 'Unreal'
		db.set_rank_fortnite(callback_query.from_user.id, data['rank'])
		await bot.send_message(callback_query.from_user.id, 'Расскажите о себе')
		await bot.answer_callback_query(callback_query.id)
		await FSMFortnite.next()

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.message_handler(state=FSMFortnite.description)
async def load_description(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['description'] = message.text
		db.set_description_fortnite(message.from_user.id, data['description'])
		await bot.send_message(message.from_user.id, 'Анкета заполнена, удачного пользования!', reply_markup = nav.mainMenu)
		await state.finish()

#----------------------------------------------------------------------------------------------------------------

#Регистрируем хендлеры
def register_handlers_fortnite(dp: Dispatcher):
	dp.register_callback_query_handler(forniteSearchAccounts, text='forniteSearchAccounts')
	dp.register_callback_query_handler(next_person, text = "next")
	dp.register_callback_query_handler(prev_person, text = "prev")
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(createFortniteAccount, text='createFortniteAccount', state = None)
	dp.register_callback_query_handler(editProfileFortnite, text='editProfileFortnite', state = None)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_message_handler(load_kd, state=FSMFortnite.kd)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_message_handler(load_pr, state=FSMFortnite.pr)
	#----------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_role_IGL, text='IGL', state=FSMFortnite.role)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_role_Fragger, text='Fragger', state=FSMFortnite.role)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_role_Support, text='Support', state=FSMFortnite.role)
	#----------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Bronze, text='BronzeFortnite', state=FSMFortnite.rank)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Silver, text='SilverFortnite', state=FSMFortnite.rank)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Gold, text='GoldFortnite', state=FSMFortnite.rank)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Platinum, text='PlatinumFortnite', state=FSMFortnite.rank)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Diamond, text='DiamondFortnite', state=FSMFortnite.rank)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Elite, text='EliteFortnite', state=FSMFortnite.rank)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Champion, text='ChampionFortnite', state=FSMFortnite.rank)
	#----------------------------------------------------------------------------------------------------------------
	dp.register_callback_query_handler(load_rank_Unreal, text='UndealFortnite', state=FSMFortnite.rank)
	#----------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------------------------------------------------------
	dp.register_message_handler(load_description, state=FSMFortnite.description)
	#----------------------------------------------------------------------------------------------------------------
	# dp.register_callback_query_handler(forniteSeartch, text='forniteSearchAccounts')

