from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMValorant(StatesGroup):
	kd = State()
	rank = State()
	description = State()
