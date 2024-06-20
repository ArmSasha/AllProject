from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import  types

def buy_menu(isUrl=True,url="",bill=""):
    qiwiMenu=InlineKeyboardMarkup(row_width=1)
    if isUrl:
        btnUrlQIwi=InlineKeyboardButton(text="Ссылка на оплату",url=url)
        qiwiMenu.add(btnUrlQIwi)
    btnCheckQIwi = InlineKeyboardButton(text="Проверить оплату", callback_data='check_' + bill)
    qiwiMenu.add(btnCheckQIwi)
    return qiwiMenu
back = types.ReplyKeyboardMarkup(resize_keyboard=True)
back.add(types.KeyboardButton('Отмена'))

apanel = types.InlineKeyboardMarkup(row_width=3)
apanel.add(types.InlineKeyboardButton(text='📢 Рассылка', callback_data='rass'))
srez2 = types.InlineKeyboardMarkup(row_width=3)
srez2.add(types.InlineKeyboardButton(text='✂️ СРЕЗ', callback_data='srez'))
men=types.InlineKeyboardMarkup(row_width=3)
men.add(types.InlineKeyboardButton(text='📢 Рассылка', callback_data='rass'))
men.add(types.InlineKeyboardButton(text='✂️ СРЕЗ', callback_data='srez'))
men.add(types.InlineKeyboardButton(text='🏧 ВДЗУ', callback_data='wdzy'))
men.add(types.InlineKeyboardButton(text='🎁 Раздача', callback_data='razdacha'))

razda = InlineKeyboardMarkup(row_width=1)
razdacha=InlineKeyboardButton(text='🎁 Раздача', callback_data='razdacha')

raz_pere=InlineKeyboardButton(text='🔀 Переключатель', callback_data='raz_pere')
razda.add(razdacha, raz_pere)

gamestavka = types.InlineKeyboardMarkup(row_width=3)
gamestavka.add(types.InlineKeyboardButton(text='✅ Согласиться', callback_data='gamestavka2'), types.InlineKeyboardButton(text='❌ Отказаться', callback_data='gamestavka1'))

help_donat2 = InlineKeyboardMarkup(row_width=3)
donat1 = InlineKeyboardButton(text='⭐️', callback_data='donat1')
donat2 = InlineKeyboardButton(text='💎 ', callback_data='donat2')
donat3 = InlineKeyboardButton(text='🔥 ', callback_data='donat3')
donat4 = InlineKeyboardButton(text='👮‍♂️ ', callback_data='donat4')
donat5 = InlineKeyboardButton(text=' 💱 Валюта ', callback_data='donat5')
donat6 = InlineKeyboardButton(text='Прочее 📁', callback_data='donat6')
donat7 = InlineKeyboardButton(text='Пополнить 🍭', callback_data='donat7')
help_donat2.add(donat1, donat2, donat3, donat4, donat5,donat6,donat7)
def uchas(count):
    kb = InlineKeyboardMarkup(row_width=1)
    kb.insert(InlineKeyboardButton(text=f'({count})✅Участвовать', callback_data='raz'))
    return kb