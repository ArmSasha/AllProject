from create_bot import dp, bot, db
from db import Database
from aiogram import types, Dispatcher
from states import FSMWelcome
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import menu_btn as btn
from keyboards import doctors_btn as doc
import config as con


#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.message_handler(commands = ['main_menu'], state = None)
async def main_menu(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_photo(call.from_user.id, caption='Меню🏠', photo = open('./Images/menu.png', 'rb'), reply_markup=btn.menu_btn)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.message_handler(commands = ['main_menu'], state = None)
async def my_data(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, f"""Ваши данные:
***Фамилия***: {db.get_surname(callback_query.from_user.id)}
***Имя***: {db.get_name(callback_query.from_user.id)}
***Отчество***: {db.get_middlename(callback_query.from_user.id)}
***Возраст***: {db.get_age(callback_query.from_user.id)}
***Пол***: {db.get_gender(callback_query.from_user.id)}
***Номер телефона***: {db.get_phone_number(callback_query.from_user.id)}
***СНИЛС***: {db.get_snils(callback_query.from_user.id)}
""", reply_markup = btn.edit_questionnaire, parse_mode='Markdown')

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------



def register_handlers_menu(dp: Dispatcher):
    dp.register_callback_query_handler(main_menu, text=['main_menu', 'back_menu'])
    dp.register_callback_query_handler(my_data, text='my_data')
    # dp.register_message_handler(load_surname, state=FSMWelcome.surname)
    # dp.register_message_handler(load_name, state=FSMWelcome.name)
    # dp.register_message_handler(load_middlename, state=FSMWelcome.middlename)
    # dp.register_message_handler(load_age, state=FSMWelcome.age)
    # dp.register_callback_query_handler(load_gender_man, text='man', state=FSMWelcome.gender)
    # dp.register_callback_query_handler(load_gender_woman, text='woman', state=FSMWelcome.gender)
    # dp.register_message_handler(load_phonenumber, state=FSMWelcome.phonenumber)
    # dp.register_message_handler(load_snils, state=FSMWelcome.snils)