'''https://t.me/AGOMarketBot - Маркет в Telegram'''
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='💵 Пополнить баланс',
                callback_data='add_balance'
            )
        ]
    ]
)
