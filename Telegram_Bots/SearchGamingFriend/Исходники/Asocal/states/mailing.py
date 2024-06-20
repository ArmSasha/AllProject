from aiogram.dispatcher.filters.state import State, StatesGroup

class bot_mailing(StatesGroup):
	text = State()
	state = State()
	photo = State()