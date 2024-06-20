import logging

from aiogram import executor

from handlers import dp
from utils import (set_default_commands,
                   connect_base,
                   close_base, db)


async def on_startup(dp):
    await set_default_commands(dp)
    await connect_base(dp)
    await db.gino.create_all()


async def on_shutdown(dp):
    await close_base(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown,
                           skip_updates=True
                           )
