import logging
import sqlite3
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
import os


API_TOKEN = '5714593221:AAE_vzYtjwfa0h7RlDO4scezpxsGQYIDWCg'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# Initialize database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_dir = (BASE_DIR + '\\likes_dislikes.db')

conn = sqlite3.connect(db_dir)
cursor = conn.cursor()
# cursor.execute("""CREATE TABLE IF NOT EXISTS likes_dislikes
#                   (id INTEGER PRIMARY KEY AUTOINCREMENT, likes INTEGER, dislikes INTEGER)""")
#conn.commit()
def user_exists(user_id):
    result = cursor.execute("SELECT * FROM likes_dislikes WHERE user_id = ?", (user_id,)).fetchall()
    return bool(len(result))

def add_user(user_id):
    cursor.execute("INSERT INTO likes_dislikes (user_id) VALUES (?)", (user_id,))

def null_like_dislike(user_id):
    #cursor.execute("INSERT INTO likes_dislikes likes = ?, dislikes = ? WHERE user_id = ? ", (0, 0, user_id,))
    cursor.execute("UPDATE likes_dislikes SET likes=?, dislikes=? WHERE user_id=?", (0, 0, user_id,))

def plus_like(likes, user_id):
    cursor.execute("UPDATE likes_dislikes SET likes=? WHERE user_id = ?", (likes, user_id,))

def set_rate(user_id):
    cursor.execute("SELECT likes, dislikes FROM likes_dislikes WHERE user_id = ?", (user_id,))


def plus_dislike(dislikes, user_id):
    cursor.execute("UPDATE likes_dislikes SET dislikes=? WHERE user_id = ?", (dislikes, user_id,))


# Define inline keyboard markup
rating_markup = InlineKeyboardMarkup(row_width=2)
rating_markup.add(InlineKeyboardButton(text="👍", callback_data="like"),
                  InlineKeyboardButton(text="👎", callback_data="dislike"))

# # Define states
# class Rating(StatesGroup):
#     rating = State()

# Define command handler
@dp.message_handler(commands=['start'])
async def start_command_handler(message: types.Message):
    if(not user_exists(message.from_user.id)):
        add_user(message.from_user.id)
        await message.reply("Привет! Оцени этот бот с помощью кнопок ниже:", reply_markup=rating_markup)
        null_like_dislike(message.from_user.id)
    else:
        await message.reply("Привет! Оцени этот бот с помощью кнопок ниже:", reply_markup=rating_markup)
        null_like_dislike(message.from_user.id)


# Define callback handler
@dp.callback_query_handler(lambda c: c.data in ['like', 'dislike'])
async def process_callback_rating(callback_query: types.CallbackQuery, state: FSMContext):
    # Get current rating
    set_rate(callback_query.from_user.id)
    likes, dislikes = cursor.fetchone()
    if callback_query.data == 'like':
        # Increment likes count
        likes += 1
        plus_like(likes, callback_query.from_user.id)
        conn.commit()
        await bot.answer_callback_query(callback_query.id, text="Спасибо за лайк!")
    elif callback_query.data == 'dislike':
        # Increment dislikes count
        dislikes += 1
        plus_dislike(dislikes, callback_query.from_user.id)
        conn.commit()
        await bot.answer_callback_query(callback_query.id, text="Спасибо за дизлайк!")
    # Update message with new rating
    set_rate(callback_query.from_user.id)
    # likes, dislikes = cursor.fetchone()
    rating_message = f"Рейтинг бота: 👍 {likes}   👎 {dislikes}"
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text=rating_message, reply_markup=rating_markup)

# Define error handler
@dp.errors_handler(exception=Exception)
async def error_handler(update, error):
    logging.exception(error)

# Start polling
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
