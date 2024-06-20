from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

backProfile = InlineKeyboardMarkup(row_width = 1)

backProfilebtn = InlineKeyboardButton(text = '⬅️ Назад', callback_data = 'backProfile')

backProfile.insert(backProfilebtn)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

editProfileFortnite = InlineKeyboardMarkup(row_width = 1)

editProfileFortnitebtn = InlineKeyboardButton(text = 'Изменить профиль', callback_data = 'editProfileFortnite')

editProfileFortnite.add(editProfileFortnitebtn, backProfilebtn)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

editProfileValorant = InlineKeyboardMarkup(row_width = 1)

editProfileValorantbtn = InlineKeyboardButton(text = 'Изменить профиль', callback_data = 'editProfileValorant')

editProfileValorant.add(editProfileValorantbtn, backProfilebtn)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

editProfileCSGO = InlineKeyboardMarkup(row_width = 1)

editProfileCSGObtn = InlineKeyboardButton(text = 'Изменить профиль', callback_data = 'editProfileCSGO')

editProfileCSGO.add(editProfileCSGObtn, backProfilebtn)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

profilebtn = InlineKeyboardMarkup(row_width = 2)

fortniteAccount = InlineKeyboardButton(text = 'Fortnite профиль', callback_data = 'fortniteAccount')
valorantAccount = InlineKeyboardButton(text = 'Valorant профиль', callback_data = 'valorantAccount')
dotaAccount = InlineKeyboardButton(text = 'Dota 2 профиль', callback_data = 'dotaAccount')
csgoAccount = InlineKeyboardButton(text = 'CS:GO профиль', callback_data = 'csgoAccount')
editProfile = InlineKeyboardButton(text = 'Изменить профиль✍️', callback_data = 'editProfile')
backMenu = InlineKeyboardButton(text = '⬅️ Назад', callback_data = 'backMenu')

profilebtn.add(fortniteAccount, valorantAccount, dotaAccount, csgoAccount, editProfile, backMenu)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

