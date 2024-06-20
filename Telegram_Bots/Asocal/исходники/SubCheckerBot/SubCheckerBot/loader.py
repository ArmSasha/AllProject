from aiogram import Bot, Dispatcher, types

from data.config import BOT_TOKEN

from utils.db_api.db_gino import db

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


__all__ = ['bot', 'dp', 'db']
