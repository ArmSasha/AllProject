from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

backGame = InlineKeyboardMarkup(row_width = 1)

btnbackGame = InlineKeyboardButton(text = '⬅️ Назад', callback_data = 'backGame')
backGame.insert(btnbackGame)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

backFortnite = InlineKeyboardMarkup(row_width = 1)

btnbackFortnite = InlineKeyboardButton(text = '⬅️ Назад', callback_data = 'backFortnite')
backFortnite.insert(btnbackFortnite)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

fortnitebtn = InlineKeyboardMarkup(row_width = 2)

arenaFortnite = InlineKeyboardButton(text = 'Соревновательный', callback_data = 'arenaFortnite')
prakiFortnite = InlineKeyboardButton(text = 'Праки', callback_data = 'prakiFortnite')
tournamentFortnite = InlineKeyboardButton(text = 'Турнир', callback_data = 'tournamentFortnite')
PGFortnite = InlineKeyboardButton(text = 'PG(1х1)', callback_data = 'PGFortnite')

fortnitebtn.add(arenaFortnite, prakiFortnite, tournamentFortnite, PGFortnite, btnbackGame)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

backValorant= InlineKeyboardMarkup(row_width = 1)

btnbackValorant = InlineKeyboardButton(text = '⬅️ Назад', callback_data = 'backValorant')
backValorant.insert(btnbackValorant)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

valorantbtn = InlineKeyboardMarkup(row_width = 2)

ratingValorant = InlineKeyboardButton(text = 'Рейтинг', callback_data = 'ratingValorant')
pablickValorant = InlineKeyboardButton(text = 'Паблик', callback_data = 'pablickValorant')
premierValorant = InlineKeyboardButton(text = 'Premier', callback_data = 'premierValorant')
prakiValorant = InlineKeyboardButton(text = 'Праки', callback_data = 'prakiValorant')

valorantbtn.add(ratingValorant, pablickValorant, premierValorant, prakiValorant, btnbackGame)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

backDota= InlineKeyboardMarkup(row_width = 1)

btnbackDota = InlineKeyboardButton(text = '⬅️ Назад', callback_data = 'backDota')
backDota.insert(btnbackDota)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

dotabtn = InlineKeyboardMarkup(row_width = 2)

ratingDota = InlineKeyboardButton(text = 'Рейтинг', callback_data = 'ratingDota')
pablickDota = InlineKeyboardButton(text = 'Паблик', callback_data = 'pablickDota')
turboDota = InlineKeyboardButton(text = 'Турбо', callback_data = 'turboDota')

dotabtn.add(ratingDota, pablickDota, turboDota, btnbackGame)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

backCSGO= InlineKeyboardMarkup(row_width = 1)

btnbackCSGO = InlineKeyboardButton(text = '⬅️ Назад', callback_data = 'backCSGO')
backCSGO.insert(btnbackCSGO)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

csgobtn = InlineKeyboardMarkup(row_width = 2)

faceitCSGO = InlineKeyboardButton(text = 'Faceit', callback_data = 'faceitCSGO')
ratingCSGO = InlineKeyboardButton(text = 'Рейтинг', callback_data = 'ratingCSGO')
prakiCSGO = InlineKeyboardButton(text = 'Праки', callback_data = 'prakiCSGO')
OnexOneCSGO = InlineKeyboardButton(text = '1x1', callback_data = 'OnexOneCSGO')

csgobtn.add(faceitCSGO, ratingCSGO, prakiCSGO, OnexOneCSGO, btnbackGame)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________
