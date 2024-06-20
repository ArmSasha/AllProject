from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMWelcome(StatesGroup):
	anonymity = State()
	text = State()
	photo = State()