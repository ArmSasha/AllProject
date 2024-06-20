import logging
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from pyqiwip2p import QiwiP2P
from db import Database
import config as con

logging.basicConfig(level=logging.INFO)

bot = Bot(token=con.TOKEN)
p2p = QiwiP2P(auth_key=con.qiwiToken)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

db = Database('database.db')
