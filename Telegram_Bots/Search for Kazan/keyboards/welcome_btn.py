from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

choice = InlineKeyboardMarkup(row_width=2)
choice.add(InlineKeyboardButton(text="Да✅", callback_data="yes"),
                  InlineKeyboardButton(text="Нет❌", callback_data="no"))

choice_anonymity = InlineKeyboardMarkup(row_width=2)
choice_anonymity.add(InlineKeyboardButton(text="Анонимно🥷", callback_data="anonymous"),
                  InlineKeyboardButton(text="Публично🙋", callback_data="publicly"))

choice_photo = InlineKeyboardMarkup(row_width=2)
choice_photo.add(InlineKeyboardButton(text="Есть", callback_data="photo_yes"),
                  InlineKeyboardButton(text="Нет", callback_data="photo_no"))