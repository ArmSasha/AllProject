from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

main_menu = InlineKeyboardMarkup(row_width=1)
main_menu.add(InlineKeyboardButton(text="Меню🏠", callback_data="main_menu"))

menu_btn = InlineKeyboardMarkup(row_width=1)
doctors = InlineKeyboardMarkup(text='Врачи👨‍⚕️', callback_data='doctors')
my_data = InlineKeyboardButton(text='Мои данные📋', callback_data='my_data')
menu_btn.add(doctors, my_data)

edit_questionnaire = InlineKeyboardMarkup(row_width=1)
edit_questionnaire.add(InlineKeyboardButton(text="Редактировать данные✍️", callback_data="edit_questionnaire"))

