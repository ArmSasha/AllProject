from create_bot import dp, bot, db
from db import Database
from aiogram import types, Dispatcher
from states import FSMWelcome
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import welcome_btn as btn
from keyboards import menu_btn as main
import config as con


#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.message_handler(commands = ['start'], state = None)
async def start(message: types.Message):
    if message.chat.type == 'private':
        if(not db.user_exists(message.from_user.id)):
            db.add_user(message.from_user.id)
            await FSMWelcome.surname.set()
            await message.answer(" Здравствуйте, я бот для записи на приём к лучшим врачам страны")
            await bot.send_message(message.from_user.id, 'Заполнение личных данных:')
            await message.reply('Укажите фамилию')
        else:
            await message.answer(" Здравствуйте, я бот для записи на приём к лучшим врачам страны")
            await message.answer(" Перейдите в меню, пожалуйста", reply_markup=main.main_menu)

    else:
        await bot.send_message(message.from_user.id, 'Бот работает только в приватных чатах!')

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='edit_questionnaire')
async def edit_questionnaire(callback_query: types.CallbackQuery):
    await FSMWelcome.surname.set()
    await bot.send_message(callback_query.from_user.id, 'Заполнение личных данных:')
    await bot.send_message(callback_query.from_user.id, 'Укажите фамилию')
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.message_handler(state=FSMWelcome.name)
async def load_surname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        db.set_surname(message.from_user.id, message.text)
        await message.answer('Укажите имя')
        await FSMWelcome.next()

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.message_handler(state=FSMWelcome.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        db.set_name(message.from_user.id, message.text)
        await message.answer('Укажите отчество')
        await FSMWelcome.next()

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.message_handler(state=FSMWelcome.name)
async def load_middlename(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        db.set_middlename(message.from_user.id, message.text)
        await message.answer('Сколько вам лет?')
        await FSMWelcome.next()

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.message_handler(state=FSMWelcome.age)
async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        age = (message.text) if message.text.isdigit() else None
        if age is not None:
            if int(age) < 0 or int(age) > 120:
                await bot.send_message(message.from_user.id, text = "Был указан некорректный возраст. Установлен возраст '0'.")
                age = "0"
                data['age'] = age
            elif len(age) > 2:
                await bot.send_message(message.from_user.id, text = "Был указан некорректный возраст. Установлен возраст '0'.")
                age = "0"
                data['age'] = age
            else:
                data['age'] = age

        db.set_age(message.from_user.id, data['age'])
        await message.answer('🚻 Укажите свой пол:', reply_markup=btn.walcome_gender)
        await FSMWelcome.next()

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='man', state=FSMWelcome.gender)
async def load_gender_man(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        db.set_gender(callback_query.from_user.id, '👨Мужчина')
        await bot.send_message(callback_query.from_user.id, 'Укажите номер телефона (в формате: 89999999999)')
        await FSMWelcome.next()

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='woman', state=FSMWelcome.gender)
async def load_gender_woman(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        db.set_gender(callback_query.from_user.id, '👩Женщина')
        await bot.send_message(callback_query.from_user.id, 'Укажите номер телефона (в формате: 89999999999)')
        await FSMWelcome.next()

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='woman', state=FSMWelcome.gender)
async def load_phonenumber(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        db.set_phone_number(message.from_user.id, message.text)
        await bot.send_message(message.from_user.id, 'Укажите номер СНИЛСа (в формате: 111-222-333-44)')
        await FSMWelcome.next()

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='woman', state=FSMWelcome.gender)
async def load_snils(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        db.set_snils(message.from_user.id, message.text)
        await bot.send_message(message.from_user.id, 'Данные заполнены, удачного пользования!', reply_markup=main.main_menu)
        await state.finish()


#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------




def register_handlers_welcome(dp: Dispatcher):
    dp.register_message_handler(start, commands = ['start'], state = None)
    dp.register_callback_query_handler(edit_questionnaire, text='edit_questionnaire')
    dp.register_message_handler(load_surname, state=FSMWelcome.surname)
    dp.register_message_handler(load_name, state=FSMWelcome.name)
    dp.register_message_handler(load_middlename, state=FSMWelcome.middlename)
    dp.register_message_handler(load_age, state=FSMWelcome.age)
    dp.register_callback_query_handler(load_gender_man, text='man', state=FSMWelcome.gender)
    dp.register_callback_query_handler(load_gender_woman, text='woman', state=FSMWelcome.gender)
    dp.register_message_handler(load_phonenumber, state=FSMWelcome.phonenumber)
    dp.register_message_handler(load_snils, state=FSMWelcome.snils)