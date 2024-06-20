# import logging
# from aiogram import Bot, Dispatcher, types, executor
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram import exceptions
# import os
# import sqlite3

# Создание экземпляров бота и диспетчера
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# db_dir = (BASE_DIR + '\\database.db')



# logging.basicConfig(level=logging.INFO)

# storage = MemoryStorage()
# dp = Dispatcher(bot, storage=storage)
# # Подключение к базе данных
# conn = sqlite3.connect(db_dir)
# cursor = conn.cursor()



# users_per_page = 3
# current_index = 0
# current_message_id = None

# # Функция для получения пользователей из базы данных
# def get_users(offset):
#     rows = cursor.execute(f"SELECT users.name, users.age, fortnite.kd, fortnite.pr, fortnite.role, fortnite.description FROM users, fortnite ON users.user_id = fortnite.user_id LIMIT {users_per_page} OFFSET {offset}").fetchall()
#     return rows if rows else []

import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import exceptions
import sqlite3
import os

logging.basicConfig(level=logging.INFO)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_dir = (BASE_DIR + '\\database.db')
bot = Bot(token='5760615918:AAHygCHZdAnKceDwVIBzhT_L-INrrbK6HbI')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
conn = sqlite3.connect(db_dir)
cursor = conn.cursor()


# users = [
#     ("User1", 25, "user1@example.com"),
#     ("User2", 30, "user2@example.com"),
#     ("User3", 35, "user3@example.com"),
#     ("User4", 40, "user4@example.com"),
#     ("User5", 45, "user5@example.com"),
#     ("User6", 50, "user6@example.com"),
# ]

users_per_page = 3
current_index = 0
current_message_id = None

def get_users(offset):
    # return users[offset:offset+users_per_page]
    rows = cursor.execute(f"SELECT users.name, users.age, fortnite.kd, fortnite.pr, fortnite.role, fortnite.description FROM users, fortnite ON users.user_id = fortnite.user_id LIMIT {users_per_page} OFFSET {offset}").fetchall()
    return rows if rows else []


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    global current_message_id
    global current_index

    current_index = 0

    offset = current_index * users_per_page
    users = get_users(offset)

    response = ""
    if users:
        for user in users:
            name, age, kd, pr, role, description = user
            response += (f"\n ____________________ \n Имя: {name} \n Возраст: {age} \n KD: {kd} \n PR: {pr} \n Role: {role} \n Описание: {description}")
    else:
        response = "Нет данных о пользователях."

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    if len(users) == users_per_page:
        next_button = types.InlineKeyboardButton("Дальше", callback_data="next")
        keyboard.add(next_button)

    if current_message_id:
        try:
            await bot.delete_message(chat_id=message.chat.id, message_id=current_message_id)
        except exceptions.MessageToDeleteNotFound:
            pass

    sent_message = await message.answer(response, reply_markup=keyboard)
    current_message_id = sent_message.message_id

@dp.callback_query_handler(lambda c: c.data == "next")
async def next_page(callback_query: types.CallbackQuery):
    global current_message_id
    global current_index

    current_index += 1

    offset = current_index * users_per_page
    users = get_users(offset)

    response = ""
    if users:
        for user in users:
            name, age, kd, pr, role, description = user
            response += (f"\n ____________________ \n Имя: {name} \n Возраст: {age} \n KD: {kd} \n PR: {pr} \n Role: {role} \n Описание: {description}")
    else:
        response = "Нет данных о пользователях."

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    if current_index > 0:
        prev_button = types.InlineKeyboardButton("Назад", callback_data="prev")
        keyboard.add(prev_button)
    if len(users) == users_per_page:
        next_button = types.InlineKeyboardButton("Дальше", callback_data="next")
        keyboard.add(next_button)

    if current_message_id:
        try:
            await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=current_message_id)
        except exceptions.MessageToDeleteNotFound:
            pass

    sent_message = await bot.send_message(callback_query.message.chat.id, response, reply_markup=keyboard)
    current_message_id = sent_message.message_id

    try:
        await callback_query.answer()
    except exceptions.MessageNotModified:
        pass

@dp.callback_query_handler(lambda c: c.data == "prev")
async def prev_page(callback_query: types.CallbackQuery):
    global current_message_id
    global current_index

    current_index -= 1

    offset = current_index * users_per_page
    users = get_users(offset)

    response = ""
    if users:
        for user in users:
            name, age, kd, pr, role, description = user
            response += (f"\n ____________________ \n Имя: {name} \n Возраст: {age} \n KD: {kd} \n PR: {pr} \n Role: {role} \n Описание: {description}")
    else:
        response = "Нет данных о пользователях."

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    if current_index > 0:
        prev_button = types.InlineKeyboardButton("Назад", callback_data="prev")
        keyboard.add(prev_button)
    if len(users) == users_per_page:
        next_button = types.InlineKeyboardButton("Дальше", callback_data="next")
        keyboard.add(next_button)

    if current_message_id:
        try:
            await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=current_message_id)
        except exceptions.MessageToDeleteNotFound:
            pass

    sent_message = await bot.send_message(callback_query.message.chat.id, response, reply_markup=keyboard)
    current_message_id = sent_message.message_id

    try:
        await callback_query.answer()
    except exceptions.MessageNotModified:
        pass

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)







# # Переменные для отслеживания текущего индекса пользователей
# current_index = 0
# users_per_page = 3
# current_message_id = None

# # Функция для получения пользователей из базы данных
# def get_users(offset):
#     rows = db.get_people_fortnite(users_per_page, offset)
#     return rows if rows else []

# # Функция для обновления информации о пользователях
# async def update_user_info(message: types.Message):
#     global current_message_id  # Объявляем current_message_id как глобальную переменную
#     offset = current_index * users_per_page
#     users = get_users(offset)

#     response = ""
#     if users:
#         for user in users:
#             name, age, kd, pr, role, description = user
#             response += (f"\n ____________________ \n Имя: {name} \n Возраст: {age} \n KD: {kd} \n PR: {pr} \n Role: {role} \n Описание: {description}")
#     else:
#         response = "Нет данных о пользователях."

#     # Проверка доступности кнопок "Дальше" и "Назад"
#     keyboard = types.InlineKeyboardMarkup(row_width=2)
#     if current_index > 0:
#         prev_button = types.InlineKeyboardButton("Назад", callback_data="prev")
#         keyboard.add(prev_button)
#     if len(users) == users_per_page:
#         next_button = types.InlineKeyboardButton("Дальше", callback_data="next")
#         keyboard.add(next_button)

#     # Обновление сообщения или отправка нового сообщения
#     if current_message_id:
#         await bot.edit_message_text(response, chat_id=message.chat.id, message_id=current_message_id, reply_markup=keyboard)
#     else:
#         sent_message = await bot.send_message(message.from_user.id, response, reply_markup=keyboard)
#         current_message_id = sent_message.message_id


# # Обработка нажатия кнопок
# # @dp.callback_query_handler(text=['next', 'prev'])
# async def handle_buttons(callback_query: types.CallbackQuery):
#     global current_index

#     # Обновление текущего индекса в зависимости от нажатой кнопки
#     if callback_query.data == 'next':
#         current_index += 1
#     elif callback_query.data == 'prev':
#         current_index -= 1

#     await update_user_info(callback_query.message)

