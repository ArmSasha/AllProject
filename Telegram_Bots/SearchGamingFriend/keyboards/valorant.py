from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

ValorantStart = InlineKeyboardMarkup(row_width = 1)

valorantAdd = InlineKeyboardButton(text = 'Создать анкету 📝', callback_data = 'createValorantAccount')
valorantSeartch = InlineKeyboardButton(text = 'Смотреть анкеты📝', callback_data = 'valorantSeartchAccounts')
btnbackGame = InlineKeyboardButton(text = '⬅️ Назад', callback_data = 'backGame')

ValorantStart.add(valorantAdd, valorantSeartch, btnbackGame)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

rank = InlineKeyboardMarkup(row_width = 2)

Iron = InlineKeyboardButton(text = 'Iron', callback_data = 'IronValorant')
Bronze = InlineKeyboardButton(text = 'Bronze', callback_data = 'BronzeValorant')
Silver = InlineKeyboardButton(text = 'Silver', callback_data = 'SilverValorant')
Gold = InlineKeyboardButton(text = 'Gold', callback_data = 'GoldValorant')
Platinum = InlineKeyboardButton(text = 'Platinum', callback_data = 'PlatinumValorant')
Diamond = InlineKeyboardButton(text = 'Diamond', callback_data = 'DiamondValorant')
Ascendant = InlineKeyboardButton(text = 'Ascendant', callback_data = 'AscendantValorant')
Immortal = InlineKeyboardButton(text = 'Immortal', callback_data = 'ImmortalValorant')

rank.add(Bronze, Silver, Gold, Platinum, Diamond, Ascendant, Immortal)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________
