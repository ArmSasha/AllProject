from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text


from keyboards import markups as nav

from create_bot import dp, db, bot


class FSMRegister(StatesGroup):
	nick = State()


#Начало диалога
# @dp.message_handler(commands = ['start'], state = None)
async def start(message: types.Message):
	if(not db.user_exists(message.from_user.id)):
		start_command = message.text
		referrer_id = str(start_command[7:])
		if str(referrer_id) != "":
			if str(referrer_id) != str(message.from_user.id):
				await FSMRegister.nick.set()
				db.add_user(message.from_user.id, referrer_id)
				try:
					await bot.send_message(referrer_id, 'По вашей ссылке зарегистрировался новый пользователь')
					"""Если что, плюшки для реферера, писать сюда"""
				except Exception as e:
					pass
				await message.reply('Укажите ваш ник')
			else:
				await bot.send_message(message.from_user.id, 'По собственной ссылке регестрироваться нельзя')
		else:
			await FSMRegister.nick.set()
			db.add_user(message.from_user.id)
			await message.reply('Укажите ваш ник')
	else:
		Logo_menu = open('Images/Logo_menu.png', 'rb')
		await bot.send_photo(message.from_user.id, caption = 'Главное меню', photo = Logo_menu, reply_markup=nav.mainMenu)
		await bot.send_message(message.from_user.id, 'Вы уже зарегистрированы!')

# @dp.message_handler(state=FSMRegister.nick)
async def load_nick(message: types.Message, state: FSMContext):

	if(len(message.text) > 15):
		await bot.send_message(message.from_user.id, 'Никнейм не должен превышать 15 символов')
	elif '@' in message.text or '/' in message.text:
		await bot.send_message(message.from_user.id, 'Вы ввели запрещёный символов')
	else:
		async with state.proxy() as data:
			data['nick'] = message.text
		db.set_nickname(message.from_user.id, message.text)
		db.set_signup(message.from_user.id, 'done')
		await state.finish()
		Logo_menu = open('Images/Logo_menu.png', 'rb')
		await bot.send_photo(message.from_user.id, caption = 'Главное меню', photo = Logo_menu, reply_markup=nav.mainMenu)

#
# # @dp.message_handler(state=FSMRegister.age)
# async def load_age(message: types.Message, state: FSMContext):
# 	async with state.proxy() as data:
# 		data['age'] = int(message.text)
# 		db.set_age(message.from_user.id, message.text)
# 		db.set_signup(message.from_user.id, 'done')
# 	await state.finish()
# 	Logo_menu = open('Images/Logo_menu.png', 'rb')
# 	await bot.send_photo(message.from_user.id, caption = 'Главное меню', photo = Logo_menu, reply_markup=nav.mainMenu)



#Вывод из состояний
# @dp.message_handler(state="*", commands='отмена')
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
	current_state = await state.get_state()
	if current_state is None:
		return
	await state.finish()
	await message.reply('OK')



#Регистрируем хендлеры
def register_handlers_condition(dp: Dispatcher):
	dp.register_message_handler(start, commands = ['start'], state = None)
	dp.register_message_handler(load_nick, state=FSMRegister.nick)
	# dp.register_message_handler(load_age, state=FSMRegister.age)
	dp.register_message_handler(cancel_handler, state="*", commands='отмена')
	dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")