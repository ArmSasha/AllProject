import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ParseMode
from aiogram.utils import markdown
from aiogram.utils.markdown import text

# Инициализация бота и хранилища состояний
bot = Bot(token='5714593221:AAE_vzYtjwfa0h7RlDO4scezpxsGQYIDWCg')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Включение логгирования
logging.basicConfig(level=logging.INFO)

# Команда /start
@dp.message_handler(Command('start'))
async def cmd_start(message: types.Message):
    """
    Инициализация состояния пользователя и вывод сообщения с кнопками "Лайк" и "Дизлайк".
    """
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton(text='👍', callback_data='like'),
               types.InlineKeyboardButton(text='👎', callback_data='dislike'))

    await message.reply("Поставьте оценку:", reply_markup=markup)

# Обработка коллбэк-кнопок "Лайк" и "Дизлайк"
@dp.callback_query_handler(lambda c: c.data in ['like', 'dislike'])
async def process_callback_kb1btn1(callback_query: types.CallbackQuery, state: FSMContext):
    """
    Обработка коллбэк-кнопок "Лайк" и "Дизлайк".
    """
    # Получение данных о состоянии кнопки (лайк или дизлайк)
    async with state.proxy() as data:
        data['choice'] = callback_query.data

        # Обновление сообщения с кнопками, удаляя клавиатуру после оценки
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text='👍', callback_data='like'),
                   types.InlineKeyboardButton(text='👎', callback_data='dislike'))

        # Вывод сообщения с текстом и обновленной клавиатурой
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text=f"Вы выбрали: {data['choice']}\nСпасибо за оценку!",
                                    reply_markup=markup)

# Запуск бота
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
