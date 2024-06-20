from create_bot import dp, bot, db, check_sub_channels
from db import Database
from aiogram import types, Dispatcher
import config as con
from keyboards import check_subscribe_btn as navs
from keyboards import menu as nav
from keyboards import welcome_btn as btn
from states import FSMWelcome
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

#----------------------------------------------------------------------------------------------------------------

# @dp.message_handler(commands = ['start'], state = None)
async def start(message: types.Message):
    if message.chat.type == 'private':
        if(not db.user_exists(message.from_user.id)):
            if await check_sub_channels(con.CHANNELS, message.from_user.id):
                db.null_block(message.from_user.id)
                db.null_like_dislike(message.from_user.id)
                db.add_user(message.from_user.id)
                await FSMWelcome.name.set()
                await message.answer("Hi, I - GamingFriendBot")
                await message.answer('Заполнение акаунта:')
                await message.reply('Укажите ваше имя')
            else:
                await bot.send_message(message.from_user.id, con.NOT_SUB_MESSAGE, reply_markup=navs.showChannels())
        else:
            if(not db.get_block(message.from_user.id)):
                Logo = open('C:/Users/Саша/PycharmProjects/KESHA/Telegram_Bots/SearchGamingFriend/Images/Logo.png', 'rb')
                await bot.send_photo(message.from_user.id, caption = 'Выберите категорию:', photo = Logo, reply_markup=nav.mainMenu)


                # await bot.send_photo(message.from_user.id, caption = 'Выберите категорию', photo = open(r'Images/Logo.png'), reply_markup=nav.mainMenu)


                # logo_menu = open('Images/logo_menu.png', 'rb')
                # await bot.send_photo(message.from_user.id, caption = 'Please click button', photo = logo_menu, reply_markup=nav.mainMenu)


                # await message.answer("Please click button", reply_markup=nav.mainMenu)

            else:
                await bot.send_message(message.from_user.id, "Вы заблокированы!")
    else:
        await bot.send_message(message.from_user.id, 'Бот работает только в приватных чатах!')

#----------------------------------------------------------------------------------------------------------------

# @dp.message_handler(text = 'editProfile', state = None)
async def editProfile(message: types.Message):
    if await check_sub_channels(con.CHANNELS, message.from_user.id):
        await FSMWelcome.name.set()
        await bot.send_message(message.from_user.id, "Заполнение акаунта:")
        await bot.send_message(message.from_user.id, 'Укажите ваше имя')
    else:
        await bot.send_message(message.from_user.id, con.NOT_SUB_MESSAGE, reply_markup=navs.showChannels())

#----------------------------------------------------------------------------------------------------------------

# @dp.message_handler(state=FSMWelcome.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        db.set_name(message.from_user.id, message.text)
        await message.answer('Введите возраст')
        await FSMWelcome.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.message_handler(state=FSMWelcome.age)
async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
        db.set_age(message.from_user.id, message.text)
        # await message.answer('Введите описание, которое будут видеть люди с которыми вы будете общаться')
        await message.answer('Выберите свой пол', reply_markup=btn.walcome_markup)
        await FSMWelcome.next()

#----------------------------------------------------------------------------------------------------------------

# # @dp.message_handler(state=FSMWelcome.text)
# async def load_text(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['text'] = message.text
#         db.set_text(message.from_user.id, message.text)
#         await message.answer('Выберите свой пол', reply_markup=btn.walcome_markup)
#         await FSMWelcome.next()

#----------------------------------------------------------------------------------------------------------------

# @dp.callback_query_handler(text='man', state=FSMWelcome.gender)
async def load_gender_man(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        # data['gender'] = message.text
        data['gender'] = 'Мужчина'
        db.set_gender(callback_query.from_user.id, data['gender'])
        await bot.send_message(callback_query.from_user.id, 'Анкета заполнена, удачного пользования!', reply_markup = nav.mainMenu)
        await bot.answer_callback_query(callback_query.id)
        await state.finish()

# @dp.callback_query_handler(text='woman', state=FSMWelcome.gender)
async def load_gender_woman(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        # data['gender'] = message.text
        data['gender'] = 'Женщина'
        db.set_gender(callback_query.from_user.id, data['gender'])
        await bot.send_message(callback_query.from_user.id, 'Анкета заполнена, удачного пользования!', reply_markup = nav.mainMenu)
        await bot.answer_callback_query(callback_query.id)
        await state.finish()



#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

#Регистрируем хендлеры
def register_handlers_welcome(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'], state = None)
    dp.register_callback_query_handler(editProfile, text = 'editProfile', state = None)
    dp.register_message_handler(load_name, state=FSMWelcome.name)
    dp.register_message_handler(load_age, state=FSMWelcome.age)
    dp.register_callback_query_handler(load_gender_man, text='man', state=FSMWelcome.gender)
    dp.register_callback_query_handler(load_gender_woman, text='woman', state=FSMWelcome.gender)
