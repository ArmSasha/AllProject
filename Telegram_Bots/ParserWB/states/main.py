from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMMain(StatesGroup):
	id = State()