from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMWelcome(StatesGroup):
	surname = State()
	name = State()
	middlename = State()
	age = State()
	gender = State()
	phonenumber = State()
	snils = State()
	