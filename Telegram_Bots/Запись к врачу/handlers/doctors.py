from create_bot import dp, bot, db
from db import Database
from aiogram import types, Dispatcher
from states import FSMWelcome
from states import FSMDoctors
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import doctors_btn as btn
import config as con

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

async def doctors(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Выберите сферу врача:", reply_markup=btn.doctors_btn)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------



async def surgeon(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Выберите врача:", reply_markup=btn.surgeon)

async def optometrist(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Выберите врача:", reply_markup=btn.optometrist)

async def speech_therapist(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Выберите врача:", reply_markup=btn.speech_therapist)

async def surgeon1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    fio = callback_query.data.split("_")[1]
    info = db.get_info(fio)
    photo = './Images/surgeon1.png'
    specialization = db.get_specialization(fio)
    await process_doctor_callback(callback_query, fio, info, photo, specialization)

async def surgeon2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    fio = callback_query.data.split("_")[1]
    info = db.get_info(fio)
    photo = './Images/surgeon2.png'
    specialization = db.get_specialization(fio)
    await process_doctor_callback(callback_query, fio, info, photo, specialization)

async def optometrist1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    fio = callback_query.data.split("_")[1]
    info = db.get_info(fio)
    photo = './Images/optometrist1.png'
    specialization = db.get_specialization(fio)
    await process_doctor_callback(callback_query, fio, info, photo, specialization)

async def optometrist2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    fio = callback_query.data.split("_")[1]
    info = db.get_info(fio)
    photo = './Images/optometrist2.png'
    specialization = db.get_specialization(fio)
    await process_doctor_callback(callback_query, fio, info, photo, specialization)

async def speech_therapist1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    fio = callback_query.data.split("_")[1]
    info = db.get_info(fio)
    photo = './Images/speech_therapist1.png'
    specialization = db.get_specialization(fio)
    await process_doctor_callback(callback_query, fio, info, photo, specialization)

async def speech_therapist2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    fio = callback_query.data.split("_")[1]
    info = db.get_info(fio)
    photo = './Images/speech_therapist2.png'
    specialization = db.get_specialization(fio)
    await process_doctor_callback(callback_query, fio, info, photo, specialization)

#----------------------------------------------------------------------------------------------------------------

async def process_doctor_callback(callback_query: types.CallbackQuery, fio, info, photo, specialization):
    # print(f"{fio}\n{info}")
    await bot.send_photo(callback_query.from_user.id, photo = open(photo, 'rb'), caption=f"Вы выбрали врача: {fio} \n{info}\nСпециальность: {specialization}", reply_markup=btn.appointment)

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

async def appointment(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Выберите дату:', reply_markup=btn.dates)
    # await bot.send_message(callback_query.from_user.id, 'Пока не сделано', reply_markup=btn.back)




#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------


async def dates(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    data = callback_query.data.split("_")[1:]
    print(f"1) {data}")
    data = str(data[0])
    print(f"2) {data}")
    # try:
    #     db.add_column(data)
    #     await bot.send_message(callback_query.from_user.id, data)
    #     await bot.send_message(callback_query.from_user.id, 'Chouse time')
    # except Exception as e: await bot.send_message(callback_query.from_user.id, e)

    # print(callback_query.data)
    # print(data)
    await appointment_doctor_callback(callback_query, data)



async def appointment_doctor_callback(callback_query: types.CallbackQuery, data):
    await bot.answer_callback_query(callback_query.id)
    print(f"3) {data}")
    try:
        db.add_column(data)
        await bot.send_message(callback_query.from_user.id, 'Chouse time')
    except Exception as e: await bot.send_message(callback_query.from_user.id, e)




#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------
def register_handlers_doctors(dp: Dispatcher):
    dp.register_callback_query_handler(dates, lambda c: c.data.startswith('date'))
    dp.register_callback_query_handler(appointment, text='appointment')
    # dp.register_callback_query_handler(appointment_doctor_callback, text='date')
    dp.register_callback_query_handler(doctors, text=['doctors', 'back'])   
    dp.register_callback_query_handler(surgeon, text='surgeon')
    dp.register_callback_query_handler(optometrist, text='optometrist')
    dp.register_callback_query_handler(speech_therapist, text='speech_therapist')
    dp.register_callback_query_handler(surgeon2, lambda c: c.data.startswith('surgeon2'))
    dp.register_callback_query_handler(surgeon1, lambda c: c.data.startswith('surgeon1'))
    dp.register_callback_query_handler(optometrist1, lambda c: c.data.startswith('optometrist1'))
    dp.register_callback_query_handler(optometrist2, lambda c: c.data.startswith('optometrist2'))
    dp.register_callback_query_handler(speech_therapist1, lambda c: c.data.startswith('speech1'))
    dp.register_callback_query_handler(speech_therapist2, lambda c: c.data.startswith('speech2'))

# async def test(message: types.Message):
    # await bot.send_message(message.from_user.id, 'Выберите время', reply_markup=btn.dates)
