import logging
import aiogram.utils.markdown as md

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram import Bot, Dispatcher, types

API_TOKEN = '5714593221:AAE_vzYtjwfa0h7RlDO4scezpxsGQYIDWCg'  # Replace with your bot token

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

logging.basicConfig(level=logging.INFO)

# Start command
@dp.message_handler(Command('start'))
async def cmd_start(message: types.Message):
    """
    Send a welcome message when the "/start" command is received.
    """
    # Send welcome message
    await bot.send_message(chat_id=message.chat.id,
                           text='Hello! This is an anonymous chat bot. You can chat with me anonymously.'
                                ' Just type your message and it will be sent without revealing your identity.')

# Message handler
@dp.message_handler()
async def process_message(message: types.Message, state: FSMContext):
    """
    Process incoming messages and send them anonymously.
    """
    # Get the text of the message
    text = message.text

    # Send the message anonymously
    await bot.send_message(chat_id=message.chat.id,
                           text='Your anonymous message: \n\n{}'.format(text))

# Start the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
