

from aiogram import types

from aiogram.dispatcher.filters import BoundFilter
#from aiogram.types import  ChatMemberRestricted
from datetime import datetime
from keyboard.main import help_perexod

register_datatime=dict()
import sqlite3
connect = sqlite3.connect("himera.db")
cursor = connect.cursor()
"""class IsRegister(BoundFilter):
    async def check(self, message):
        user_id = message.from_user.id
        cursor.execute(f"SELECT user_id FROM users WHERE user_id = {user_id}")
        if cursor.fetchone() is None:
            need_seconds = 86400
            current_time = datetime.now()
            last_datetime = register_datatime.get(message.from_user.id)
            register_datatime[message.from_user.id] = current_time

            # Если первое сообщение (время не задано)
            if not last_datetime:
                register_datatime[message.from_user.id] = current_time
                last_datetime = datetime.fromtimestamp(0)
            if last_datetime:
                # Разница в секундах между текущим временем и временем последнего сообщения
                delta_seconds = (current_time - last_datetime).total_seconds()

                # Осталось ждать секунд перед отправкой
                seconds_left = int(need_seconds - delta_seconds)
                # Если время ожидания не закончилось
                if seconds_left > 0:
                    pass
                else:
                    register_datatime[message.from_user.id] = current_time
                    name1 = message.from_user.get_mention(as_html=True)
                    await message.reply(
                        f' 👋 Добро пожаловать  {name1}\n🎳 Я - игровой бот Химера!\n\n<b>Чтобы пользоваться командами бота напишите /start в Личные Сообщения бота</b>',
                        reply_markup=help_perexod, parse_mode='html')
                    return False
        else:
            return True"""
class IsRegister2(BoundFilter):
    async def check(self, message):
        user_id = message.from_user.id
        cursor.execute(f"SELECT user_id FROM users WHERE user_id = {user_id}")
        if cursor.fetchone() is None:
            name1 = message.from_user.get_mention(as_html=True)
            await message.reply(
                f' 👋 Добро пожаловать  {name1}\n🎳 Я - игровой бот Химера!\n\n<b>Чтобы пользоваться командами бота напишите /start в Личные Сообщения бота</b>',
                reply_markup=help_perexod, parse_mode='html')
            return False
        else:
            return True
class IsRegister3(BoundFilter):
    async def check(self, callback: types.CallbackQuery):
        user_id = callback.from_user.id
        user_name_new = callback.from_user.full_name
        cursor.execute(f"SELECT user_id FROM users WHERE user_id = {user_id}")
        if cursor.fetchone() is None:
            await callback.message.answer(
                f' 👋 Добро пожаловать  <a href="tg://user?id={user_id}">{user_name_new}</a> \n🎳 Я - игровой бот Химера!\n\n<b>Чтобы пользоваться командами бота напишите /start в Личные Сообщения бота</b>',
                reply_markup=help_perexod, parse_mode='html')
            return False
        else:
            return True