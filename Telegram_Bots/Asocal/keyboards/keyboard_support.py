from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types


def fun(user_id):
    quest = types.InlineKeyboardMarkup(row_width=3)
    quest.add(
        types.InlineKeyboardButton(text='💬 Ответить', callback_data=f'{user_id}-ans'),
        types.InlineKeyboardButton(text='❎ Удалить', callback_data='ignor')
    )
    return quest

back = types.ReplyKeyboardMarkup(resize_keyboard=True)
back.add(
    types.KeyboardButton('⏪ Отмена')
)

support = InlineKeyboardMarkup(row_width=1)
support.add(
    types.InlineKeyboardButton(text='Написать в тех.поддержку', callback_data = 'support'),
    types.InlineKeyboardButton(text = '⬅️ Назад', callback_data = 'back')
    )