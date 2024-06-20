from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

forniteStart = InlineKeyboardMarkup(row_width = 1)

forniteAdd = InlineKeyboardButton(text = 'Создать анкету 📝', callback_data = 'createFortniteAccount')
forniteSeartch = InlineKeyboardButton(text = 'Смотреть анкеты📝', callback_data = 'forniteSearchAccounts')
btnbackGame = InlineKeyboardButton(text = '⬅️ Назад', callback_data = 'backGame')

forniteStart.add(forniteAdd, forniteSeartch, btnbackGame)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

rolebtn = InlineKeyboardMarkup(row_width = 1)

IGL = InlineKeyboardButton(text = 'IGL (In game leader)', callback_data = 'IGL')
Fragger = InlineKeyboardButton(text = 'Fragger', callback_data = 'Fragger')
Support = InlineKeyboardButton(text = 'Support', callback_data = 'Support')

rolebtn.add(IGL, Fragger, Support)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

rankbtn = InlineKeyboardMarkup(row_width = 2)

Bronze = InlineKeyboardButton(text = 'Bronze', callback_data = 'BronzeFortnite')
Silver = InlineKeyboardButton(text = 'Silver', callback_data = 'SilverFortnite')
Gold = InlineKeyboardButton(text = 'Gold', callback_data = 'GoldFortnite')
Platinum = InlineKeyboardButton(text = 'Platinum', callback_data = 'PlatinumFortnite')
Diamond = InlineKeyboardButton(text = 'Diamond', callback_data = 'DiamondFortnite')
Elite = InlineKeyboardButton(text = 'Elite', callback_data = 'EliteFortnite')
Champion = InlineKeyboardButton(text = 'Champion', callback_data = 'ChampionFortnite')
Unreal = InlineKeyboardButton(text = 'Unreal', callback_data = 'UndealFortnite')

rankbtn.add(Bronze, Silver, Gold, Platinum, Diamond, Elite, Champion, Unreal)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________
