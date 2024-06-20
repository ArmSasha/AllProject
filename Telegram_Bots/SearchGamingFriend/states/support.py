from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMSupport(StatesGroup):
	item = State()
	text = State()