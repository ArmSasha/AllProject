from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMWelcome(StatesGroup):
	name = State()
	age = State()
	gender = State()