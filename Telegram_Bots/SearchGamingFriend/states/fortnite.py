from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMFortnite(StatesGroup):
	kd = State()
	pr = State()
	role = State()
	rank = State()
	description = State()
