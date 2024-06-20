from create_bot import dp, bot, db, check_sub_channels
from db import Database
from aiogram import types, Dispatcher
from states import FSMWelcome
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import config as con
from keyboards import welcome_btn as nav
from keyboards import check_subscribe_btn as navs
from keyboards import admins_btn as btn
import datetime
# from keyboards import client_btn as nav








# @dp.message_handler(commands = ['start'], state = None)
async def start(message: types.Message):
    if message.chat.type == 'private':
        if(not db.user_exists(message.from_user.id)):
                if await check_sub_channels(con.CHANNELS, message.from_user.id):
                    db.add_user(message.from_user.id)
                    db.null_block(message.from_user.id)
                    db.set_date(message.from_user.id, datetime.datetime.now())
                    db.null_num_questionnaires(message.from_user.id)
                    await message.answer("Здравствуйте, желаете оставить заявку на поиск человека?", reply_markup=nav.choice)
                    # await bot.send_message(message.from_user.id, 'Заполнение анкетки:')
                    # await message.reply('Как я могу обращаться к тебе?🤔')

                else:
                    await bot.send_message(message.from_user.id, con.NOT_SUB_MESSAGE, reply_markup=navs.showChannels())
        else:
            if(not db.get_block(message.from_user.id)):
                await message.answer("Здравствуйте, желаете оставить заявку на поиск человека?", reply_markup=nav.choice)
            else:
                await bot.send_message(message.from_user.id, "Вы заблокированы!")

    else:
        await bot.send_message(message.from_user.id, 'Бот работает только в приватных чатах!')

# #----------------------------------------------------------------------------------------------------------------
# #----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='edit_questionnaire')
async def choice_yes(callback_query: types.CallbackQuery, state: FSMContext):
    if db.get_block(callback_query.from_user.id) == 0:
        await bot.send_message(callback_query.from_user.id, 'Заполнение анкеты:')
        await bot.send_message(callback_query.from_user.id, 'Как опубликовать пост?', reply_markup = nav.choice_anonymity)
        db.add_questionnaires(callback_query.from_user.id)
        await FSMWelcome.anonymity.set()
    else:
        await bot.send_message(message.from_user.id, "Вы заблокированы!")

# @dp.callback_query_handler(text='edit_questionnaire')
async def choice_no(callback_query: types.CallbackQuery):
    if db.get_block(callback_query.from_user.id) == 0:
        await bot.send_message(callback_query.from_user.id, 'Создание анкеты отменено!')
    else:
        await bot.send_message(message.from_user.id, "Вы заблокированы!")

# #----------------------------------------------------------------------------------------------------------------
# #----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='edit_questionnaire')
async def choice_anonymity_anon(callback_query: types.CallbackQuery, state: FSMContext):
    if db.get_block(callback_query.from_user.id) == 0:
        await FSMWelcome.next()
        db.set_anonymity(callback_query.from_user.id, 0)
        await bot.send_message(callback_query.from_user.id, 'Пост будет опубликован анонимно!')
        await bot.send_message(callback_query.from_user.id, 'Введите текст анкеты: (не более 500 символов)')
    else:
        await bot.send_message(message.from_user.id, "Вы заблокированы!")

# @dp.callback_query_handler(text='edit_questionnaire')
async def choice_anonymity_pabl(callback_query: types.CallbackQuery):
    if db.get_block(callback_query.from_user.id) == 0:
        await FSMWelcome.next()
        db.set_anonymity(callback_query.from_user.id, callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, 'Пост будет опубликован публично!')
        await bot.send_message(callback_query.from_user.id, 'Введите текст анкеты: (не более 500 символов)')
    else:
        await bot.send_message(message.from_user.id, "Вы заблокированы!")

# #----------------------------------------------------------------------------------------------------------------
# #----------------------------------------------------------------------------------------------------------------


# @dp.message_handler(state=FSMWelcome.text)
async def set_text(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        max_length = 500  # Максимальное количество символов
        text = message.text
        if len(text) > max_length:
            # await bot.send_photo(message.from_user.id, caption = 'Ваше сообщение было отформатировано, так как превышает разрешённые 500 символов. Вы всегда можете изменить свою анкету!', photo = open('Images/404.png', 'rb'))
            await message.answer('Ваше сообщение было отформатировано, так как превышает разрешённые 500 символов')
            text = text[:max_length]
            data['text'] = text
            # await message.reply("Ваше сообщение было отформатировано, так как превышает максимальное количество символов.")
        else:
            data['text'] = text
        db.set_text(message.from_user.id, text)
        await message.answer('У вас есть фотография человека, которого вы ищите?', reply_markup = nav.choice_photo)
        await FSMWelcome.next()

# #----------------------------------------------------------------------------------------------------------------
# #----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='edit_questionnaire')
async def choice_photo_yes(callback_query: types.CallbackQuery):
    if db.get_block(callback_query.from_user.id) == 0:
        await bot.send_message(callback_query.from_user.id, 'Пришлите фото')
    else:
        await bot.send_message(message.from_user.id, "Вы заблокированы!")

# @dp.callback_query_handler(text='edit_questionnaire')
async def choice_photo_no(callback_query: types.CallbackQuery, state: FSMContext):
    if db.get_block(callback_query.from_user.id) == 0:
        await bot.send_message(callback_query.from_user.id, 'Анкета была отправлена на подтверждение админу!')
        await state.finish()
        await bot.send_message(1030874842, f"Text: {db.get_text(callback_query.from_user.id)} \nAnon: {db.get_anonymity(callback_query.from_user.id)}", reply_markup = btn.admins_choise)
    else:
        await bot.send_message(message.from_user.id, "Вы заблокированы!")

# #----------------------------------------------------------------------------------------------------------------
# #----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='edit_questionnaire')
async def set_photo(callback_query: types.CallbackQuery, state: FSMContext):
    if db.get_block(callback_query.from_user.id) == 0:
        db.set_photo(callback_query.from_user.id, messages.photo[-1].file_id)
        await bot.send_message(callback_query.from_user.id, 'Анкета была отправлена на подтверждение админу!')
        await bot.send_photo(1030874842, caption = f"Text: {db.get_text(callback_query.from_user.id)} \nAnon: {db.get_anonymity(callback_query.from_user.id)}", photo =  db.get_photo_id(callback_query.from_user.id), reply_markup = btn.admins_choise) 
        await state.finish()

    else:
        await bot.send_message(message.from_user.id, "Вы заблокированы!")


# # @dp.message_handler(state=FSMWelcome.name)
# async def load_name(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         max_length = 50  # Максимальное количество символов
#         text = message.text
#         if len(text) > max_length:
#             await bot.send_photo(message.from_user.id, caption = 'Ваше сообщение было отформатировано, так как превышает разрешённые 50 символов. Вы всегда можете изменить свою анкету!', photo = open('Images/404.png', 'rb'))
#             text = text[:max_length]
#             data['name'] = text
#             # await message.reply("Ваше сообщение было отформатировано, так как превышает максимальное количество символов.")
#         else:
#             data['name'] = text
#         db.set_name(message.from_user.id, text)
#         await message.answer('Сколько тебе лет?🔞')
#         await FSMWelcome.next()

# #----------------------------------------------------------------------------------------------------------------

# # @dp.message_handler(state=FSMWelcome.age)
# async def load_age(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         age = (message.text) if message.text.isdigit() else None
#         if age is not None:
#             if int(age) < 0 or int(age) > 120:
#                 await bot.send_photo(message.from_user.id, caption = "Был указан некорректный возраст. Установлен возраст '0'.", photo = open('Images/404.png', 'rb'))
#                 age = "0"
#                 data['age'] = age
#                 # await message.reply("Был указан некорректный возраст. Установлен возраст '0'.")
#             elif len(age) > 2:
#                 await bot.send_photo(message.from_user.id, caption = "Был указан некорректный возраст. Установлен возраст '0'.", photo = open('Images/404.png', 'rb'))
#                 age = "0"
#                 data['age'] = age
#             else:
#                 data['age'] = age

#         # age = message.text.strip()  # Удаляем возможные пробелы вокруг введенного возраста
#         # if not age.isdigit():
#         #     formatted_text = "0"
#         #     await bot.send_photo(message.from_user.id, caption = 'Был указан некорректный возраст. Установлен возраст '0'.', photo = open('Images/404.png', 'rb'))
#         #     data['age'] = formatted_text
#         # else:
#         #     data['age'] = age

#         db.set_age(message.from_user.id, age)
#         await message.answer('💬 Расскажи немного о себе, кого ты ищешь, чем увлекаешься и т.д.')
#         await FSMWelcome.next()

# #----------------------------------------------------------------------------------------------------------------


# #----------------------------------------------------------------------------------------------------------------

# # @dp.callback_query_handler(text='man', state=FSMWelcome.gender)
# async def load_gender_man(callback_query: types.CallbackQuery, state: FSMContext):
#     async with state.proxy() as data:
#         # data['gender'] = message.text
#         data['gender'] = '👨Парень'
#         db.set_gender(callback_query.from_user.id, data['gender'])
#         await bot.send_message(callback_query.from_user.id, 'Анкета заполнена, удачного общения!')
#         await bot.send_message(callback_query.from_user.id, """📜 Правила чата. Прочти перед использованием:
# 1. Уважайте других участников✊
# 2. Сохраняйте анонимность🎭
# 3. Не публикуйте незаконный контент🔞
# 4. Избегайте спама и рекламы📢

# 📝 Помните, что администрация бота имеет право изменять правила по своему усмотрению для обеспечения комфортного опыта для всех участников.""", reply_markup=nav.find_partner)
#         await state.finish()

# # @dp.callback_query_handler(text='woman', state=FSMWelcome.gender)
# async def load_gender_woman(callback_query: types.CallbackQuery, state: FSMContext):
#     async with state.proxy() as data:
#         # data['gender'] = message.text
#         data['gender'] = '👩Девушка'
#         db.set_gender(callback_query.from_user.id, data['gender'])
#         await bot.send_message(callback_query.from_user.id, 'Анкета заполнена, удачного общения!')
#         await bot.send_message(callback_query.from_user.id, """📜 Правила чата. Прочти перед использованием:
# 1. Уважайте других участников✊
# 2. Сохраняйте анонимность🎭
# 3. Не публикуйте незаконный контент🔞
# 4. Избегайте спама и рекламы📢

# 📝 Помните, что администрация бота имеет право изменять правила по своему усмотрению для обеспечения комфортного опыта для всех участников.""", reply_markup=nav.find_partner)
#         await state.finish()


# #----------------------------------------------------------------------------------------------------------------

# # # @dp.message_handler(state=FSMWelcome.gender)
# # async def load_gender(message: types.Message, state: FSMContext):
# #     async with state.proxy() as data:
# #         # data['gender'] = message.text
# #         db.set_gender(message.from_user.id, data['gender'])
# #         await message.answer('Анкета заполнена, удачного общения!', reply_markup=nav.find_partner)
# #         await state.finish()



# # # @dp.message_handler(commands=['start'])
# # async def start(message: types.Message):
# #     if message.chat.type == 'private':
# #         if await check_sub_channels(con.CHANNELS, message.from_user.id):
# #             await message.answer(" Привет, я Анонимный ЧатБот!")
# #             await message.answer(" Пожалуйста нажмите на кнопку для поиска нового собеседника", reply_markup=nav.find_partner)
# #         else:
# #             await bot.send_message(message.from_user.id, con.NOT_SUB_MESSAGE, reply_markup=nav.showChannels())

# #----------------------------------------------------------------------------------------------------------------

# #Регистрируем хендлеры
def register_handlers_welcome(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'], state = None)
    dp.register_callback_query_handler(choice_yes, text='yes', state = None)
    dp.register_callback_query_handler(choice_no, text='no', state = None)
    dp.register_callback_query_handler(choice_anonymity_anon, text='anonymous', state = FSMWelcome.anonymity)
    dp.register_callback_query_handler(choice_anonymity_pabl, text='publicly', state = FSMWelcome.anonymity)
    dp.register_message_handler(set_text, state = FSMWelcome.text)
    dp.register_callback_query_handler(choice_photo_yes, text='photo_yes', state = None)
    dp.register_callback_query_handler(choice_photo_no, text='photo_no', state = FSMWelcome.photo)
    dp.register_callback_query_handler(set_photo, state = FSMWelcome.photo)

#     dp.register_message_handler(load_name, state=FSMWelcome.name)
#     dp.register_message_handler(load_age, state=FSMWelcome.age)
#     dp.register_callback_query_handler(load_gender_man, text='man', state=FSMWelcome.gender)
#     dp.register_callback_query_handler(load_gender_woman, text='woman', state=FSMWelcome.gender)
