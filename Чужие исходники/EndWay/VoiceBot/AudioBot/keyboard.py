from aiogram import types

buttons = types.InlineKeyboardMarkup(row_width=3)
buttons.add(types.InlineKeyboardButton(text='❤️‍🔥 Добавить бота', url="https://telegram.me/end_soft?startgroup=new")) 

apanel = types.InlineKeyboardMarkup(row_width=3)
apanel.add(types.InlineKeyboardButton(text='📢 Рассылка пользователям', callback_data='rass'))
apanel.add(types.InlineKeyboardButton(text='📢 Рассылка в чаты', callback_data='rass_chat'))
apanel.add(types.InlineKeyboardButton(text='📊 Статистика', callback_data='stats'))

back = types.ReplyKeyboardMarkup(resize_keyboard=True)
back.add(types.KeyboardButton('Отмена'))