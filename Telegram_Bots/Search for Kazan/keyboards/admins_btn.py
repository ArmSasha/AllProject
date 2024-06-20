from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

admins_choise = InlineKeyboardMarkup(row_width=2)
admins_choise.add(InlineKeyboardButton(text="Да✅", callback_data="yes"),
                  InlineKeyboardButton(text="Нет❌", callback_data="no"))