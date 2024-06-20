from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMDoctors(StatesGroup):
    waiting_for_date = State()
    waiting_for_time = State()