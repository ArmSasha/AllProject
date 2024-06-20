from create_bot import dp, bot
from aiogram import types, Dispatcher
import parser
from states import FSMMain
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


async def start(message: types.Message):
	await bot.send_message(message.from_user.id, 'Кинь ссылку на товар')
	await FSMMain.id.set()


async def get_item_id(message: types.Message, state: FSMContext):
	url = message.text.lower()
	if url == 'отмена':
		state.finish()
	else:
		parser.ParseWB(url).parse()
		try:
			await bot.send_message(message.from_user.id, 'Ok')
		except Exception as e:
			raise e
		await state.finish()

#Регистрируем хендлеры
def register_handlers_main(dp: Dispatcher):
	dp.register_message_handler(start, commands = ['start'], state = None)
	dp.register_message_handler(get_item_id, state = FSMMain.id)
	# dp.register_message_handler(load_nick, state=FSMRegister.nick)
	# # dp.register_message_handler(load_age, state=FSMRegister.age)
	# dp.register_message_handler(cancel_handler, state="*", commands='отмена')
	# dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")