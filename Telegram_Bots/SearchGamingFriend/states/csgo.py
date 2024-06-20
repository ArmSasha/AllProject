from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMCSGO(StatesGroup):
	faceit = State()
	rank = State()
	description = State()
