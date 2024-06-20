from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

mainMenu = InlineKeyboardMarkup(row_width = 2) # resize_keyboard = True

btnGames = InlineKeyboardButton(text = '🎮 Игры', callback_data = 'games')
btnProfile = InlineKeyboardButton(text='💳 Профиль', callback_data = 'profile') #
btnSupport = InlineKeyboardButton(text='👨‍💻Поддержка', callback_data = 'support_text')

mainMenu.add(btnGames, btnProfile, btnSupport)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

backMenu = InlineKeyboardMarkup(row_width = 1)

btnbackMenu = InlineKeyboardButton(text = '⬅️ Назад', callback_data = 'backMenu')
backMenu.insert(btnbackMenu)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

gamesMenu = InlineKeyboardMarkup(row_width = 2)

fortnite = InlineKeyboardButton(text = 'Fortnite', callback_data = 'fortnite')
valorant = InlineKeyboardButton(text = 'Valorant', callback_data = 'valorant')
dota = InlineKeyboardButton(text = 'Dota 2', callback_data = 'dota')
csgo = InlineKeyboardButton(text = 'CS:GO', callback_data = 'csgo')

gamesMenu.add(fortnite, valorant, dota, csgo, btnbackMenu)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________
