'''https://t.me/AGOMarketBot - Маркет в Telegram'''
import logging

from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

from data import BOT_TOKEN
from handlers.errors import register_errors
from handlers.callbacks import register_callbacks
from handlers.commands import register_commands
from utils import set_default_commands
from utils.database import create_base


def register_handlers(dp: Dispatcher):
    register_commands(dp)
    register_callbacks(dp)
    register_errors(dp)


async def on_startup(dp: Dispatcher):
    await create_base()
    register_handlers(dp)
    await set_default_commands(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
    dp = Dispatcher(bot, storage=MemoryStorage())
    executor.start_polling(dp, on_startup=on_startup)
