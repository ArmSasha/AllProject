from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

CSGOStart = InlineKeyboardMarkup(row_width = 1)

CSGOAdd = InlineKeyboardButton(text = 'Создать анкету 📝', callback_data = 'createCSGOAccount')
CSGOSeartch = InlineKeyboardButton(text = 'Смотреть анкеты📝', callback_data = 'CSGOSeartchAccounts')
btnbackGame = InlineKeyboardButton(text = '⬅️ Назад', callback_data = 'backGame')

CSGOStart.add(CSGOAdd, CSGOSeartch, btnbackGame)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

faceitbtn = InlineKeyboardMarkup(row_width = 2)

lvl1 = InlineKeyboardButton(text = 'LVL 1', callback_data = 'lvl1')
lvl2 = InlineKeyboardButton(text = 'LVL 2', callback_data = 'lvl2')
lvl3 = InlineKeyboardButton(text = 'LVL 3', callback_data = 'lvl3')
lvl4 = InlineKeyboardButton(text = 'LVL 4', callback_data = 'lvl4')
lvl5 = InlineKeyboardButton(text = 'LVL 5', callback_data = 'lvl5')
lvl6 = InlineKeyboardButton(text = 'LVL 6', callback_data = 'lvl6')
lvl7 = InlineKeyboardButton(text = 'LVL 7', callback_data = 'lvl7')
lvl8 = InlineKeyboardButton(text = 'LVL 8', callback_data = 'lvl8')
lvl9 = InlineKeyboardButton(text = 'LVL 9', callback_data = 'lvl9')
lvl10 = InlineKeyboardButton(text = 'LVL 10', callback_data = 'lvl10')


faceitbtn.add(lvl1, lvl2, lvl3, lvl4, lvl5, lvl6, lvl7, lvl8, lvl9, lvl10)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

rankbtn = InlineKeyboardMarkup(row_width = 2)

Silver = InlineKeyboardButton(text = 'Сильвер', callback_data = 'SilverCSGO')
Goldnova = InlineKeyboardButton(text = 'Голднова', callback_data = 'GoldnovaCSGO')
Kalash = InlineKeyboardButton(text = 'Голднова', callback_data = 'KalashCSGO')
Bigstar = InlineKeyboardButton(text = 'Калаш', callback_data = 'BigstarCSGO')
Golden_Eagle = InlineKeyboardButton(text = 'Бигстар', callback_data = 'Golden_EagleCSGO')
Supreme = InlineKeyboardButton(text = 'Беркут', callback_data = 'SupremeCSGO')
Global = InlineKeyboardButton(text = 'Глобал', callback_data = 'GlobalCSGO')

rankbtn.add(Silver, Goldnova, Kalash, Bigstar, Golden_Eagle, Supreme, Global)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

Silverbtn = InlineKeyboardMarkup(row_width = 2)

Silver1 = InlineKeyboardButton(text = 'Silver I', callback_data = 'Silver1')
Silver2 = InlineKeyboardButton(text = 'Silver II', callback_data = 'Silver2')
Silver3 = InlineKeyboardButton(text = 'Silver III', callback_data = 'Silver3')
Silver4 = InlineKeyboardButton(text = 'Silver IV', callback_data = 'Silver4')
Silver5 = InlineKeyboardButton(text = 'Silver V', callback_data = 'Silver5')
Silver_Elit_Master = InlineKeyboardButton(text = 'Silver Elite Master', callback_data = 'Silver_Elit_Master')

Silverbtn.add(Silver1, Silver2, Silver3, Silver4, Silver5, Silver_Elit_Master)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

Goldnovabtn = InlineKeyboardMarkup(row_width = 2)

Goldnova1 = InlineKeyboardButton(text = 'Gold Nova I', callback_data = 'Goldnova1')
Goldnova2 = InlineKeyboardButton(text = 'Gold Nova II', callback_data = 'Goldnova2')
Goldnova3 = InlineKeyboardButton(text = 'Gold Nova III', callback_data = 'Goldnova3')
GoldNova_Master = InlineKeyboardButton(text = 'Gold Nova Master', callback_data = 'GoldNova_Master')

Goldnovabtn.add(Goldnova1, Goldnova2, Goldnova3, GoldNova_Master)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

Kalashbtn = InlineKeyboardMarkup(row_width = 2)

Kalash1 = InlineKeyboardButton(text = 'Master Guardian I', callback_data = 'Kalash1')
Kalash2 = InlineKeyboardButton(text = 'Master Guardian II', callback_data = 'Kalash2')
Kalash3 = InlineKeyboardButton(text = 'Master Guardian Elite', callback_data = 'Kalash3')

Kalashbtn.add(Kalash1, Kalash2, Kalash3)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________

Golden_Eagle_btn = InlineKeyboardMarkup(row_width = 2)

Golden_Eagle1 = InlineKeyboardButton(text = 'Legendary Eagle', callback_data = 'Golden_Eagle1')
Golden_Eagle2 = InlineKeyboardButton(text = 'Legendary Eagle Master', callback_data = 'Golden_Eagle2')

Golden_Eagle_btn.add(Golden_Eagle1, Golden_Eagle2)

#_________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________
