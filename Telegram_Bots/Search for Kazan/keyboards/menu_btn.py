from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types


back_main = InlineKeyboardMarkup(row_width=1)
back_main_btn = InlineKeyboardButton(text='Меню🏠', callback_data = 'back_main')
back_main.add(back_main_btn)

#----------------------------------------------------------------------------------------------------------------

questionnaire = InlineKeyboardMarkup(row_width=1)
edit_questionnaire = InlineKeyboardButton(text='Изменить анкету ✍️', callback_data='edit_questionnaire')
achievements = InlineKeyboardButton(text='Достижения 🏆', callback_data = 'achievements')
questionnaire.add(edit_questionnaire, achievements)

achievements = InlineKeyboardMarkup(row_width=1)
quantity_messages = InlineKeyboardButton(text='Проверить количество сообщений', callback_data='quantity_messages')
promo_code = InlineKeyboardButton(text='Проверить промокод', callback_data='promo_code')
achievements.add(quantity_messages, promo_code, back_main_btn)