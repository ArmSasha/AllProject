from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
help_mine = InlineKeyboardMarkup(row_width=4)
mine = InlineKeyboardButton(text='⛏️ Копать руду', callback_data='mine')
help_mine.add(mine)

help_ferma = InlineKeyboardMarkup(row_width=3)
fermasnat = InlineKeyboardButton(text='Снять Фантомы 💠', callback_data='fermasnat')
help_ferma.add(fermasnat)

help_mine2 = InlineKeyboardMarkup(row_width=3)
mine2 = InlineKeyboardButton(text='⛏️ Копать руду', callback_data='mine')
bag = InlineKeyboardButton(text='🎒 Инвентарь', callback_data='bag')
help_mine2.add(mine2,bag)
help_biz = InlineKeyboardMarkup(row_width=3)
bizsnat = InlineKeyboardButton(text='💸 Снять прибыль', callback_data='bizsnat')
help_biz.add(bizsnat)

back_menuadmin = InlineKeyboardMarkup(row_width=3)
back_menuadmin2= InlineKeyboardButton(text='⬅️ Назад', callback_data='back_menuadmins')
back_menuadmin.add(back_menuadmin2)

help_city = InlineKeyboardMarkup(row_width=1)
earning = InlineKeyboardButton(text='⏰️Заработок', callback_data='earning')
ore_recycling = InlineKeyboardButton(text='♻️Переработка руды', callback_data='ore_recycling')
help_city.add(earning,ore_recycling)

back_city = InlineKeyboardMarkup(row_width=1)
back_city1 = InlineKeyboardButton(text='◀️ В Город', callback_data='back_city')
back_city.add(back_city1)

oer_sell = InlineKeyboardMarkup(row_width=3)
ferum = InlineKeyboardButton(text='1️⃣', callback_data='oersell_1')
gold = InlineKeyboardButton(text='2️⃣', callback_data='oersell_2')
dioumond = InlineKeyboardButton(text='3️⃣', callback_data='oersell_3')
ametist = InlineKeyboardButton(text='4️⃣', callback_data='oersell_4')
aquamarin = InlineKeyboardButton(text='5️⃣', callback_data='oersell_5')
emerald = InlineKeyboardButton(text='6️⃣', callback_data='oersell_6')
back_city1 = InlineKeyboardButton(text='◀️ В Город', callback_data='back_city')
oer_sell.add(ferum,gold,dioumond,ametist,aquamarin,emerald,back_city1)

def oer_cycl(name: int):
    kb = InlineKeyboardMarkup(row_width=1)
    back_city3 = InlineKeyboardButton(text='◀️ Назад', callback_data='ore_recycling')
    aell=InlineKeyboardButton(text='♻️ Переработать', callback_data=f'oer_{name}')
    kb.add(aell,back_city3)
    return kb

earning_sell = InlineKeyboardMarkup(row_width=3)
car = InlineKeyboardButton(text='1️⃣', callback_data='ear_1')
plane = InlineKeyboardButton(text='2️⃣', callback_data='ear_2')
yacht = InlineKeyboardButton(text='3️⃣', callback_data='ear_3')
vertolet = InlineKeyboardButton(text='4️⃣', callback_data='ear_4')
house = InlineKeyboardButton(text='5️⃣', callback_data='ear_5')
back_city1 = InlineKeyboardButton(text='◀️ В Город', callback_data='back_city')
earning_sell.add(car,plane,yacht,vertolet,house,back_city1)
def ear_work(name: int):
    kb1 = InlineKeyboardMarkup(row_width=1)
    back_city3 = InlineKeyboardButton(text='◀️ Назад', callback_data='earning')
    aerell=InlineKeyboardButton(text='Сдать в Аренду', callback_data=f'earwork_{name}')
    kb1.add(aerell,back_city3)
    return kb1